from functools import cached_property
import pandas as pd


from atapi import API


class Data(API):
    """Obtain Data From Various Sources"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    MC_BASE = 'https://www.binance.com'
    MC_EP = '/exchange-api/v2/public/asset-service/product/get-products'
    TR_BASE = 'https://api.fiscaldata.treasury.gov/services/api/fiscal_service/'
    TR_EP = 'v2/accounting/od/avg_interest_rates?sort=-record_date&page[size]=1'
    API_BASE = 'https://api.binance.com'
    TIME = "/api/v3/time"

    columns = ('Open time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close time',
               'Quote asset volume', 'Number of trades', 'Taker buy base asset volume',
               'Taker buy quote asset volume', 'Ignore')

    def klines(self, symbol: str, interval: str, **kwargs):
        """Kijun Line"""

        params = {"symbol": symbol, "interval": interval, **kwargs}
        return self.query(self.API_BASE+"/api/v3/klines", params)

    @property
    def rfr(self):
        """Riskfree Return: T-Bill Average Interest Rate"""
        response = self.query(self.TR_BASE+self.TR_EP)
        data = response['data'][0]['avg_interest_rate_amt']
        return float(data)/100

    @property
    def circulating_supply(self):
        """Circulating Supply"""
        response = self.query(self.MC_BASE+self.MC_EP)
        data = response['data']
        return pd.Series({item['s']: item['cs'] for item in data if item['s'].endswith('USDT')},
                         name='Circulating Supply')

    @property
    def symbols(self):
        """Ticker Symbols"""
        _symbols = self.circulating_supply.index.values.tolist()
        return _symbols[:3]

    def servertime(self):
        """Returns the servertime.
    If your systemtime is off, synchronize with timeserver."""
        # TODO exception when time is out of sync
        return pd.to_datetime(self.query(self.API_BASE+self.TIME)['serverTime'], unit='ms')

    @cached_property
    def assets(self):
        """Assets, all columns"""
        _assets = pd.concat((pd.DataFrame(self.klines(symbol, "1d"),
                                          columns=self.columns).set_index('Open time')
                            for symbol in self.symbols), axis=1, keys=self.symbols)
        _assets = _assets.swaplevel(axis=1)  # Swapping levels for selection
        _assets.index = pd.to_datetime(_assets.index, unit='ms')
        _assets.index.name = 'Date'
        return _assets
