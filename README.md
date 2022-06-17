# Algorithmic Trading Framework

This framework backtests, forward tests and deploys trading algorithms and strategies on binance spot, futures and nft markets and other cryptocurrency exchanges, including arbitrage.

- Daily Close Prices
- Daily Logarithmic Returns, Mean Returns
- Tangency Portfolio with optimal weights
- Market Capitalisation
- Annualised Risk σ, Variance and Return
- Correlation Matrix and Covariance
- Systematic & Unsystematic Variance
- Sharpe, beta, CAPM, alpha

## Installation 
```sh
pip install atapi 
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
Run:
```sh
python -m atf
```
```sh
Welcome to the Algorithmic Trading Framework. Type help or ? for commands.

atf🖖
```

## Examples (See Wiki for More)
```sh
atf🖖 help

Documented commands (type help <topic>):
========================================
assets_close        correlation  marketcap_summary  returns      stats_mcap
balance             covariance   mean_returns       servertime   weights_cwi
bye                 help         normalized         stats        weights_ewi
circulating_supply  marketcap    optimal_weights    stats_index  weights_pwi
```
```sh
atf🖖 returns
            BTCUSDT  ETHUSDT  BNBUSDT  XRPUSDT  TRXUSDT  LTCUSDT      TP
Date
2021-01-23  -0.0267   0.0008   0.0004  -0.0018   0.0235   0.0001  0.0004
2021-01-24   0.0057   0.1212   0.0221   0.0063   0.0250   0.0240  0.0221
2021-01-25  -0.0002  -0.0551   0.0002  -0.0215  -0.0168  -0.0283  0.0002
2021-01-26   0.0066   0.0358   0.0001   0.0029   0.0000  -0.0177  0.0001
2021-01-27  -0.0669  -0.0975  -0.0231  -0.0692  -0.0437  -0.0952 -0.0231
...             ...      ...      ...      ...      ...      ...     ...
2022-06-01  -0.0648  -0.0660  -0.0660  -0.0578  -0.0101  -0.0870 -0.0660
2022-06-02   0.0215   0.0088   0.0260   0.0187   0.0091   0.0283  0.0260
2022-06-03  -0.0250  -0.0327  -0.0320  -0.0379  -0.0389  -0.0299 -0.0320
2022-06-04   0.0055   0.0165   0.0090   0.0054  -0.0083   0.0174  0.0090
2022-06-05  -0.0003   0.0005  -0.0013   0.0025  -0.0022   0.0016 -0.0013

[499 rows x 7 columns]
```
```sh
atf🖖 correlation
         BTCUSDT  ETHUSDT  BNBUSDT  XRPUSDT  TRXUSDT  LTCUSDT     TP
BTCUSDT   1.0000   0.8185   0.6730   0.6215   0.6770   0.8043 0.6730
ETHUSDT   0.8185   1.0000   0.6970   0.6390   0.6892   0.8268 0.6970
BNBUSDT   0.6730   0.6970   1.0000   0.5832   0.6057   0.6896 1.0000
XRPUSDT   0.6215   0.6390   0.5832   1.0000   0.6422   0.7094 0.5832
TRXUSDT   0.6770   0.6892   0.6057   0.6422   1.0000   0.7249 0.6057
LTCUSDT   0.8043   0.8268   0.6896   0.7094   0.7249   1.0000 0.6896
TP        0.6730   0.6970   1.0000   0.5832   0.6057   0.6896 1.0000
```
```sh
atf🖖 stats
         Return   Risk  Sharpe  Variance  Sys. Var.  Unsys. Var.   beta   CAPM   alpha
BTCUSDT -0.0721 0.7503 -0.1374    0.5630     0.6433      -0.0803 0.3964 0.5978 -0.6699
ETHUSDT  0.2794 0.9686  0.2564    0.9382     0.8600       0.0782 0.5299 0.7887 -0.5093
BNBUSDT  1.4609 1.2739  1.1224    1.6229     1.6229      -0.0000 1.0000 1.4609  0.0000
XRPUSDT  0.2698 1.3363  0.1787    1.7857     0.9929       0.7928 0.6118 0.9058 -0.6359
TRXUSDT  0.7560 1.1559  0.6272    1.3360     0.8919       0.4441 0.5496 0.8168 -0.0608
LTCUSDT -0.5629 1.1156 -0.5324    1.2445     0.9801       0.2644 0.6039 0.8945 -1.4574
TP       1.4609 1.2739  1.1224    1.6229     1.6229      -0.0000 1.0000 1.4609  0.0000
```
## Development

Run:
```sh
cd atapi
pip install .[dev]
```

## Project 

https://github.com/streetyoga/atapi

## License

[MIT](LICENSE.txt)
