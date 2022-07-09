"""connection tests"""
from atapi.comp.algo import requests, DataFetch


def test_connection():
    """test mainnet API connection"""
    assert 'serverTime' in DataFetch.client.time()


def test_supply():
    """test connection to supply url"""
    response = requests.get(DataFetch.MC_URL)
    assert str(response) == "<Response [200]>"


def test_riskfree_return():
    """test connection to treasury url"""
    response = requests.get(DataFetch.TR_URL)
    assert str(response) == "<Response [200]>"
