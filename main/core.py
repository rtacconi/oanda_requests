import requests
import json
import math
import pandas as pd
from main.utils import flatten


def is_error(status_code):
    '''
    Check if an HTTP code is an error or not
    Args:
    status_code (int): returned from an HTTP call, it could be 401, 503 or 200

    Returns:
    bool: true if the code is an error
    '''
    status_code = int(status_code)
    return math.floor(status_code / 100) == 4 or math.floor(status_code / 100) == 5

def headers(access_token):
    return {
        'Authorization': "Bearer {}".format(access_token),
        'Content-type': 'application/json', 'Accept': 'text/plain'
    }

def http_call(method, uri, access_token, data={}):
    if len(data) > 0:
        data = json.dumps(data)

    try:
        if method == 'GET':
            r = requests.get(uri, headers=headers(access_token))
        elif method == 'PUT':
            r = requests.put(uri, data=data, headers=headers(access_token))
        elif method == 'POST':
            r = requests.post(uri, data=data, headers=headers(access_token))
        else:
            return {}
    except requests.exceptions.RequestException as e:
        return (500, e)
        pass

    if is_error(r.status_code):
        return (r.status_code, r.json()['errorMessage'])
    else:
        return (r.status_code, r.json())

def price_data(config, instrument, price, granularity, start, end, end_time=None):
    uri = "https://{}/v3/instruments/{}/candles?price={}&granularity={}".format(config['url'], instrument, price, granularity)
    if end_time:
        delta = "&from={}T00%3A00%3A00.000000000Z&to={}T{}.000000000Z".format(start, end, end_time)
    else:
        delta = "&from={}T00%3A00%3A00.000000000Z&to={}T23%3A59%3A59.000000000Z".format(start, end)
    uri = uri + delta
    result = http_call('GET', uri, config['access_token'])
    data = []

    if not is_error(result[0]):
        for row in result[1]['candles']:
            data.append(flatten(row))
        df = pd.DataFrame(data)

        if len(df) == 0:
            return pd.DataFrame()
        else:
            del df['complete']
            df = df.set_index(df['time'])
            del df['time']
            return df
    else:
        return pd.DataFrame()

def market_order(config, instrument, units):
    data = {
        "order": {
            "units": units,
            "instrument": instrument,
            "timeInForce": "FOK",
            "type": "MARKET",
            "positionFill": "DEFAULT"
        }
    }
    uri = "https://{}/v3/accounts/{}/orders".format(config['url'], config['account_id'])
    return http_call('POST', uri, config['access_token'], data)

def market_order_trailing(config, instrument, units, distance):
    data = {
        "order": {
            "units": units,
            "instrument": instrument,
            "timeInForce": "FOK",
            "type": "MARKET",
            "positionFill": "DEFAULT",
            "trailingStopLossOnFill": {
                "distance": distance
            }
        }
    }
    uri = "https://{}/v3/accounts/{}/orders".format(
        config['url'],
        config['account_id']
    )
    return http_call('POST', uri, config['access_token'], data)


def market_order_trailing_risk(config, instrument, units, risk):
    price = get_last_ask_price(config, instrument)
    distance = round (float(price) * float(risk), 2)
    return market_order_trailing(config, instrument, units, distance)


def get_id_from_market_order(r):
    return r[1]['lastTransactionID']


def get_pricing(config, instruments):
    endpoint = "pricing?instruments={}".format(instruments)
    uri = "https://{}/v3/accounts/{}/{}".format(config['url'], config['account_id'], endpoint)
    return http_call('GET', uri, config['access_token'])

def get_last_ask_price(config, instruments):
    r = get_pricing(config, instruments)
    return float(r[1]['prices'][0]['asks'][0]['price'])

def get_trades(config, ids):
    endpoint = "trades?ids={}".format(ids)
    uri = "https://{}/v3/accounts/{}/{}".format(config['url'], config['account_id'], endpoint)
    return http_call('GET', uri, config['access_token'])

def is_trade_on(config, ids):
    '''
    Check if a Trade is still running on Onada
    Parameters:
    dict: Configuration with account id, url and access token
    str: the trade id, if an interger is passed, it is converted to a string

    Retruns:
    int: an integer >= than 0, 0 if the API did not return a trade or usually 1 (trade found).
    '''
    return len(get_trades(config, str(ids))[1]['trades'])

def get_open_trades(config):
    endpoint = "openTrades"
    uri = "https://{}/v3/accounts/{}/{}".format(config['url'], config['account_id'], endpoint)
    return http_call('GET', uri, config['access_token'])

def get_open_trades_by_instrument(config, instrument):
    r = get_open_trades(config)
    trades = []

    if r[0] == 200:
        for trade in r[1]['trades']:
            if trade['instrument'] == instrument:
                trades.append(trade)

    return trades

def total_units_by_instrument(config, instrument):
    trades = get_open_trades_by_instrument(config, instrument)
    total_units = 0

    for trade in trades:
        total_units = total_units + int(trade['currentUnits'])

    return total_units

def is_tradeable(config, instrument):
    '''
    Check if we can trade an instrument
    Args:
    config(dict): dictionary with url, account_id and access_token
    instrument(str): the instrument we are interested in
    '''
    r = get_pricing(config, instrument)
    return r[1]['prices'][0]['tradeable']

def close_trade(config, id, units=0):
    if units < 0:
        raise ValueError('You cannot pass a negative value for units')

    endpoint = "trades/{}/close".format(id)
    uri = "https://{}/v3/accounts/{}/{}".format(config['url'], config['account_id'], endpoint)

    if units > 0:
        r = http_call('PUT', uri, config['access_token'], units=units)
    else:
        r = http_call('PUT', uri, config['access_token'])

    return r

def get_account(config):
    uri = "https://{}/v3/accounts/{}".format(config['url'], config['account_id'])
    return http_call('GET', uri, config['access_token'])
