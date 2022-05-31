"""Binance API client"""
from binance.spot import Spot as Client


def test_connection():
    """test connection"""
    client = Client()
    client.time()
