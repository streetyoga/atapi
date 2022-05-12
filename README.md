# atf - Algorithmic Trading Framework

This project backtests, forward tests and deploys trading algorithms and strategies on binance spot, futures and nft markets and other cryptocurrency exchanges, including arbitrage.

- Market Capitalisation
- Annualised Risk σ, Variance and Return
- Correlation Matrix and Covariance
- Optimal Sharpe Portfolio
- Systematic & Unsystematic Variance
- beta, CAPM, alpha

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

## Examples

```python
>>> import atf

>>> atf.servertime # Time on Binance testserver
Timestamp('2022-05-12 11:48:20.183000')

>>> atf.balance # Balance on Binance testserver
  asset             free      locked
0   BNB    1000.00000000  0.00000000
1   BTC       1.00000000  0.00000000
2  BUSD   10000.00000000  0.00000000
3   ETH     100.00000000  0.00000000
4   LTC     500.00000000  0.00000000
5   TRX  500000.00000000  0.00000000
6  USDT   10000.00000000  0.00000000
7   XRP   50000.00000000  0.00000000

>>> atf.assets_close # Daily Close Prices
              BTCUSDT   ETHUSDT  BNBUSDT  LTCUSDT  TRXUSDT  XRPUSDT
Date
2022-05-04 39695.8000 2940.6700 402.6000 106.4000   0.0863   0.6461
2022-05-05 36551.0400 2747.9300 378.5000  96.9000   0.0745   0.5983
2022-05-06 35844.5400 2655.3300 157.0700  95.6000   0.0817   0.5813
2022-05-07 35472.3900 2637.3300 365.5000  94.5000   0.0835   0.5818
2022-05-08 34035.0000 2519.5100 356.0000  94.0000   0.0880   0.5662
2022-05-09 30092.4300 2227.2500 296.4000  76.0000   0.0727   0.4865
2022-05-10 31017.1000 2786.6700 319.2000  78.7000   0.0730   0.4864
2022-05-11 29098.2900 2000.0000 271.6000  92.2000   0.0730   0.4880
2022-05-12 28402.0900 1950.1700 270.0000  62.9000   0.0717   0.4890

>>> atf.marketcap # Daily market capitalisation of all coins on testnet
                     BTCUSDT           ETHUSDT             BNBUSDT            LTCUSDT       TRXUSDT       XRPUSDT
Date
2022-05-04 755714468999.4000 206631159044.9800 39530969948467.8047 5143705967360.7998 14090802.9425 78012369.5351
2022-05-05 695845650798.7200 193087956443.4200 37164610346485.5000 4684446505989.2998 12170665.7165 72240830.6653
2022-05-06 682395556019.2200 186581260579.0200 15422576874828.2090 4621600474433.2002 13334830.5483 70188191.3183
2022-05-07 675310697176.7700 185316460087.0200 35888150810146.5000 4568423063116.5000 13631994.6427 70248563.0638
2022-05-08 647946179505.0000 177037638199.9400 34955353456668.0000 4544251512518.0000 14360209.9512 68364964.6042
2022-05-09 572888939342.4900 156501494211.5000 29103277428529.1992 3674075690972.0000 11875134.3918 58741708.3715
2022-05-10 590492476695.2999 195810088168.9800 31341991076877.5977 3804602064203.8999 11915953.6355 58729634.0224
2022-05-11 553962856930.4700 140533388000.0000 26668185389974.8008 4457233930363.4004 11915953.6355 58922823.6080
2022-05-12 540708849873.8700 137031998637.9800 26511082677810.0000 3040781065291.2998 11698795.2588 59043567.0990

>>> atf.returns # Daily returns, including tangency portfolio
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

>>> atf.mean_returns # Mean returns over testnet period
BTCUSDT   -0.0413
ETHUSDT   -0.0513
BNBUSDT   -0.0480
LTCUSDT   -0.0657
TRXUSDT   -0.0233
XRPUSDT   -0.0348
dtype: float64

>>> atf.correlation # Correlation matrix
         BTCUSDT  ETHUSDT  BNBUSDT  LTCUSDT  TRXUSDT  XRPUSDT
BTCUSDT   1.0000   0.6878   0.2120   0.2887   0.7533   0.8035
ETHUSDT   0.6878   1.0000   0.2045  -0.1622   0.1850   0.1829
BNBUSDT   0.2120   0.2045   1.0000  -0.0037  -0.0909   0.2522
LTCUSDT   0.2887  -0.1622  -0.0037   1.0000   0.4572   0.3381
TRXUSDT   0.7533   0.1850  -0.0909   0.4572   1.0000   0.7900
XRPUSDT   0.8035   0.1829   0.2522   0.3381   0.7900   1.0000

>>> atf.optimal_weights # Optimal weights for tangency portfolio
BTCUSDT   0.0000
ETHUSDT   0.0000
BNBUSDT   1.0000
LTCUSDT   0.0000
TRXUSDT   0.0000
XRPUSDT   0.0000
dtype: float64

>>> atf.covar # Annualized covariance
         BTCUSDT  ETHUSDT  BNBUSDT  LTCUSDT  TRXUSDT  XRPUSDT      TP
BTCUSDT   0.8077   1.8020   1.7050   0.8256   1.2483   0.7520  1.7050
ETHUSDT   1.8020   8.4996   5.3378  -1.4974   0.9944   0.5557  5.3378
BNBUSDT   1.7050   5.3378  80.1968  -0.0676  -1.4996   2.3488 80.1968
LTCUSDT   0.8256  -1.4974  -0.0676  10.0317   2.6699   1.1158 -0.0676
TRXUSDT   1.2483   0.9944  -1.4996   2.6699   3.3990   1.5177 -1.4996
XRPUSDT   0.7520   0.5557   2.3488   1.1158   1.5177   1.0857  2.3488
TP        1.7050   5.3378  80.1968  -0.0676  -1.4996   2.3488 80.1968

>>> atf.stats # Various key statistics
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
