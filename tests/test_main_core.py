"""
Test oanda_requests by creating a configuration and making real requests to
Oanda. Oanda account and access token have to be specified by environment
variables. It is quite obvious but you should use an Oanda Practise account
to avoid trading fees.
"""

import os
from unittest.mock import MagicMock
import main.core as oanda

ACCOUNT_ID = os.environ['ACCOUNT_ID']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']

CONFIG = {
    'account_id': ACCOUNT_ID,
    'access_token': ACCESS_TOKEN,
    'url': 'api-fxpractice.oanda.com'
}

def test_get_pricing_with_correct_instrument():
    """
    Get price information when passing a corrent instrument
    """
    res = oanda.get_pricing(CONFIG, 'SPX500_USD')
    assert res[0] == 200
    assert isinstance(res[1], dict)
    # we want a price as result
    assert len(res[1]['prices']) > 0

def test_get_pricing_with_incorrect_instrument():
    """
    Get price information when passing a incorrent instrument
    """
    res = oanda.get_pricing(CONFIG, 'XXX500_WRONG')
    assert res[0] == 400

def test_get_account_to_return_basic_info(get_account_response):
    oanda.http_call = MagicMock(return_value=get_account_response)
    res = oanda.get_account(CONFIG)
    assert res[0] == 200
    assert isinstance(res[1], dict)
    assert 'hedgingEnabled' in res[1]['account']
    assert 'currency' in res[1]['account']
    assert 'lastTransactionID' in res[1]['account']
    assert 'orders' in res[1]['account']
