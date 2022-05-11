# atf - Algorithmic Trading Framework

This project backtests, forward tests and deploys trading algorithms and strategies on binance spot, futures and nft markets and other cryptocurrency exchanges, including arbitrage.

- Annualised Risk σ, Variance and Return
- Correlation Matrix and Covariance
- Optimal Sharpe Portfolio
- Systematic & Unsystematic Variance
- beta, CAPM, alpha

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
Install dependencies:
```
pip install -r requirements.txt
```
Instructions on how to setup a your API key for the spot testnet:

[Binance Spot API Key](https://dev.binance.vision/t/9)

Export as environment variables:

Bash/Sh/Zsh:    
```sh                           
export BINANCE_API_KEY='your_api_key'           
export BINANCE_API_SECRET='your_secret_key'      

# Check
echo $BINANCE_API_KEY
echo $BINANCE_API_SECRET
```

Powershell:   
```powershell                                 
$env:BINANCE_API_KEY = 'your_api_key'          
$env:BINANCE_API_SECRET = 'your_secret_key'    

# Check
$env:BINANCE_API_KEY
$env:BINANCE_API_KEY
```

Either run interactively in an editor that supports `# %%` syntax like vscode or pyCharm

Or start in your console:

Windows:
```
py atf/atf.py
```
Linux:
```
python3 atf/atf.py
```
## Development

Run:
```
make test
```
For Windows install WSL and a distro like kali, then run: 
```
kali run make test
```


## Project 

https://github.com/streetyoga/atf

## License

[MIT](LICENSE.txt)
