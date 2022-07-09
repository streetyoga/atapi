"""connection tests"""
from atapi.comp.algo import Algo, requests


def test_connection():
    """test mainnet API connection"""
    assert 'serverTime' in Algo.client.time()


def test_supply():
    """test connection to supply url"""
    response = requests.get(Algo.MC_URL)
    assert str(response) == "<Response [200]>"


def test_riskfree_return():
    """test connection to treasury url"""
    response = requests.get(Algo.TR_URL)
    assert str(response) == "<Response [200]>"
