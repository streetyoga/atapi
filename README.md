# atf - Algorithmic Trading Framework

This project backtests, forward tests and deploys trading algorithms and strategies on binance spot, futures and nft markets and other cryptocurrency exchanges, including arbitrage.

## Examples

```python
>>> import atf
>>> atf.key('')
>>> atf.secret('')
>>> atf.strategy.buy_and_hold()
>>> atf.algo.sma(amount = 0, position = None)
>>> atf.algo.sma(trendlines = [200, 50], position = 50, asset = 'BTCUSDT')
>>> atf.algo.ema(position = 100, short = True, asset = 'ETHUSDT')

```
## Installation 
Install dependencies in the requirements.txt file manually:
```
pip install -r requirements.txt
```
Or run the cell in the notebook to install the dependencies (commented by default)
```python
# Uncomment (Ctrl+/) to install dependencies
# %pip install pandas binance-connector
```

## Development

Run `make test`  
For Windows install WSL and a distro like kali, then run `kali run make test`


## Project 

https://github.com/streetyoga/atf

## License

[MIT](LICENSE.txt)
