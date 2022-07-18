"""connection tests"""
from atapi.cmp.algo import Algo
import datetime

algo = Algo()


def test_connection():
    """test mainnet API connection"""
    assert isinstance(algo.servertime(), datetime.datetime)


def test_supply():
    """test connection to supply url"""
    response = algo.query(algo.MC_BASE+algo.MC_EP)
    assert response['data'][0]['s'] == 'BNBBTC'


def test_riskfree_return():
    """test connection to treasury url"""
    response = algo.query(algo.TR_BASE+algo.TR_EP)
    assert 'avg_interest_rate_amt' in response['data'][0]
