"""Binance API client"""
from binance.spot import Spot as Client
import requests
MC_BASE = 'https://www.binance.com'
MC_PATH = '/exchange-api/v2/public/asset-service/product/get-products'
MC_URL = MC_BASE + MC_PATH  # For Circulating Supply Data


def test_connection():
    """test mainnet API connection"""
    client = Client()
    assert 'serverTime' in client.time()


def test_supply():
    """test connection to supply url"""
    response = requests.get(MC_URL)
    print(response)
    assert str(response) == "<Response [200]>"
