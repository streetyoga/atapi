"""connection tests"""
from atapi.comp.algo import requests, client, MC_URL, TR_URL


def test_connection():
    """test mainnet API connection"""
    assert 'serverTime' in client.time()


def test_supply():
    """test connection to supply url"""
    response = requests.get(MC_URL)
    assert str(response) == "<Response [200]>"


def test_riskfree_return():
    """test connection to treasury url"""
    response = requests.get(TR_URL)
    assert str(response) == "<Response [200]>"
