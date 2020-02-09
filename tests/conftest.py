"""
Prepare mocked data for testing the Oanda API client
"""
import pytest

def testing():
    return True

@pytest.fixture(scope="module")
def get_account_response():
    """
    Return mocked anwser from this Oanda endpoint:
    https://developer.oanda.com/rest-live-v20/account-ep/
    """
    return (
        200,
        {
            'account': {
                'guaranteedStopLossOrderMode': 'DISABLED',
                'hedgingEnabled': False,
                'id': '101-004-5885399-001',
                'createdTime': '2017-04-27T21:44:54.166620114Z',
                'currency': 'GBP',
                'createdByUserID': 5885399,
                'alias': 'Primary',
                'marginRate': '0.1',
                'lastTransactionID': '139734',
                'balance': '9998.4972',
                'openTradeCount': 1,
                'openPositionCount': 1,
                'pendingOrderCount': 0,
                'pl': '-28046.3005',
                'resettablePL': '-28046.3005',
                'resettablePLTime': '2017-04-27T21:44:54.166620114Z',
                'financing': '-6000.5123',
                'commission': '0.0000',
                'dividendAdjustment': '0',
                'guaranteedExecutionFees': '0.0000',
                'orders': [],
                'positions': [
                    {
                        'instrument': 'EUR_USD',
                        'long': {
                            'units': '0',
                            'pl': '723.8162',
                            'resettablePL': '723.8162',
                            'financing': '-54.9415',
                            'dividendAdjustment': '0',
                            'guaranteedExecutionFees': '0.0000',
                            'unrealizedPL': '0.0000'
                        },
                        'short': {
                            'units': '0',
                            'pl': '0.0000',
                            'resettablePL': '0.0000',
                            'financing': '0',
                            'dividendAdjustment': '0',
                            'guaranteedExecutionFees': '0.0000',
                            'unrealizedPL': '0.0000'
                        },
                        'pl': '723.8162',
                        'resettablePL': '723.8162',
                        'financing': '-54.9415',
                        'commission': '0.0000',
                        'dividendAdjustment': '0',
                        'guaranteedExecutionFees': '0.0000',
                        'unrealizedPL': '0.0000',
                        'marginUsed': '0.0000'
                    },
                    {
                        'instrument': 'BCO_USD',
                        'long': {
                            'units': '0',
                            'pl': '-0.0236',
                            'resettablePL': '-0.0236',
                            'financing': '0.0000',
                            'dividendAdjustment': '0',
                            'guaranteedExecutionFees': '0.0000',
                            'unrealizedPL': '0.0000'
                        },
                        'short': {
                            'units': '0',
                            'pl': '0.0000',
                            'resettablePL': '0.0000',
                            'financing': '0.0000',
                            'dividendAdjustment': '0',
                            'guaranteedExecutionFees': '0.0000',
                            'unrealizedPL': '0.0000'
                        },
                        'pl': '-0.0236',
                        'resettablePL': '-0.0236',
                        'financing': '0.0000',
                        'commission': '0.0000',
                        'dividendAdjustment': '0',
                        'guaranteedExecutionFees': '0.0000',
                        'unrealizedPL': '0.0000',
                        'marginUsed': '0.0000'
                    },
                ],
                'trades': [
                    {
                        'id': '139732',
                        'instrument': 'SPX500_USD',
                        'price': '3334.8',
                        'openTime': '2020-02-07T11:25:15.217773556Z',
                        'initialUnits': '-10',
                        'initialMarginRequired': '2578.4000',
                        'state': 'OPEN',
                        'currentUnits': '-10',
                        'realizedPL': '0.0000',
                        'financing': '-1.6127',
                        'dividendAdjustment': '0.0000',
                        'unrealizedPL': '75.9419',
                        'marginUsed': '2578.0000'
                    }
                ],
                'unrealizedPL': '75.9419',
                'NAV': '10074.4391',
                'marginUsed': '2578.0000',
                'marginAvailable': '7496.4391',
                'positionValue': '25780.0000',
                'marginCloseoutUnrealizedPL': '77.5368',
                'marginCloseoutNAV': '10076.0340',
                'marginCloseoutMarginUsed': '2578.0000',
                'marginCloseoutPositionValue': '25780.0000',
                'marginCloseoutPercent': '0.12793',
                'withdrawalLimit': '7496.4391',
                'marginCallMarginUsed': '2578.0000',
                'marginCallPercent': '0.25585'
                },
            'lastTransactionID': '139734'
        }
    )
