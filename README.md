# atf - Algorithmic Trading Framework

This project backtests, forward tests and deploys trading algorithms and strategies on binance spot, futures and nft markets and other cryptocurrency exchanges, including arbitrage.

- Daily Close Prices
- Daily Logarithmic Returns, Mean Returns
- Tangency Portfolio with optimal weights
- Market Capitalisation
- Annualised Risk σ, Variance and Return
- Correlation Matrix and Covariance
- Systematic & Unsystematic Variance
- Sharpe, beta, CAPM, alpha

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

Windows:
```
cd atf
py
```
```python
>>> import atf as at
```
Linux:
```
cd atf
python3
```
```python
>>> import atf as at
```

## Examples (See Wiki for More)

```python
>>> atf.servertime # Time on Binance testserver
Timestamp('2022-05-12 11:48:20.183000')

>>> at.balance # Balance on Binance testserver
  asset             free      locked
0   BNB    1000.00000000  0.00000000
1   BTC       1.00000000  0.00000000
2  BUSD   10000.00000000  0.00000000
3   ETH     100.00000000  0.00000000
4   LTC     500.00000000  0.00000000
5   TRX  500000.00000000  0.00000000
6  USDT   10000.00000000  0.00000000
7   XRP   50000.00000000  0.00000000

>>> at.returns # Daily returns, including tangency portfolio
            BTCUSDT  ETHUSDT  BNBUSDT  LTCUSDT  TRXUSDT  XRPUSDT      TP
Date
2022-05-05  -0.0825  -0.0678  -0.0617  -0.0935  -0.1465  -0.0769 -0.0617
2022-05-06  -0.0195  -0.0343  -0.8795  -0.0135   0.0914  -0.0288 -0.8795
2022-05-07  -0.0104  -0.0068   0.8446  -0.0116   0.0220   0.0009  0.8446
2022-05-08  -0.0414  -0.0457  -0.0263  -0.0053   0.0520  -0.0272 -0.0263
2022-05-09  -0.1231  -0.1233  -0.1832  -0.2126  -0.1900  -0.1517 -0.1832
2022-05-10   0.0303   0.2241   0.0741   0.0349   0.0034  -0.0002  0.0741
2022-05-11  -0.0639  -0.3317  -0.1615   0.1583   0.0000   0.0033 -0.1615
2022-05-12  -0.0242  -0.0252  -0.0059  -0.3824  -0.0184   0.0020 -0.0059

>>> at.correlation # Correlation matrix
         BTCUSDT  ETHUSDT  BNBUSDT  LTCUSDT  TRXUSDT  XRPUSDT
BTCUSDT   1.0000   0.6878   0.2120   0.2887   0.7533   0.8035
ETHUSDT   0.6878   1.0000   0.2045  -0.1622   0.1850   0.1829
BNBUSDT   0.2120   0.2045   1.0000  -0.0037  -0.0909   0.2522
LTCUSDT   0.2887  -0.1622  -0.0037   1.0000   0.4572   0.3381
TRXUSDT   0.7533   0.1850  -0.0909   0.4572   1.0000   0.7900
XRPUSDT   0.8035   0.1829   0.2522   0.3381   0.7900   1.0000

>>> at.stats # Various key statistics
          Return   Risk   Sharpe  Variance  Sys. Var.  Unsys. Var.    beta     CAPM    alpha
BTCUSDT -15.7346 0.8987 -17.5427    0.8077     1.7050      -0.8973  0.0213  -0.3535 -15.3811
ETHUSDT -18.7520 2.9154  -6.4427    8.4996     5.3378       3.1618  0.0666  -1.1728 -17.5792
BNBUSDT -18.0550 8.9553  -2.0196   80.1968    80.1968      -0.0000  1.0000 -18.0550   0.0000
LTCUSDT -23.9996 3.1673  -7.5871   10.0317    -0.0676      10.0993 -0.0008   0.0462 -24.0459
TRXUSDT  -9.0579 1.8436  -4.9299    3.3990    -1.4996       4.8986 -0.0187   0.3692  -9.4271
XRPUSDT -12.7195 1.0420 -12.2368    1.0857     2.3488      -1.2631  0.0293  -0.4987 -12.2208
TP      -18.0550 8.9553  -2.0196   80.1968    80.1968      -0.0000  1.0000 -18.0550   0.0000
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
