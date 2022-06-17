"""connection tests"""
from atapi.comp.algo import requests, client, MC_URL


def test_connection():
    """test mainnet API connection"""
    assert 'serverTime' in client.time()


def test_supply():
    """test connection to supply url"""
    response = requests.get(MC_URL)
    assert str(response) == "<Response [200]>"
