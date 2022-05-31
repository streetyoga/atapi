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
```sh
cd atf
pip install . 
```
Instructions on how to setup a your API key for the spot testnet:

[Binance Spot API Key](https://dev.binance.vision/t/9)

Export as environment variables and run interpreter:

Bash/Sh/Zsh:    
```sh                           
export BINANCE_API_KEY='your_api_key'           
export BINANCE_API_SECRET='your_secret_key'      

# Check
echo $BINANCE_API_KEY
echo $BINANCE_API_SECRET

python3
```
```python
>>> import atf
```

Powershell:   
```powershell                                 
$env:BINANCE_API_KEY = 'your_api_key'          
$env:BINANCE_API_SECRET = 'your_secret_key'    

# Check
$env:BINANCE_API_KEY
$env:BINANCE_API_KEY

py
```
```python
>>> import atf
```

## Examples (See Wiki for More)
```python
>>> atf.returns # Daily returns, including tangency portfolio
            BTCUSDT  ETHUSDT  BNBUSDT  XRPUSDT  TRXUSDT  LTCUSDT      TP
Date
2021-01-08   0.0288  -0.0065  -0.0283  -0.0111  -0.0179   0.0166 -0.0283
2021-01-09  -0.0123   0.0474   0.0346   0.0120   0.1066   0.0290  0.0346
2021-01-10  -0.0496  -0.0172  -0.0335  -0.0290  -0.0321  -0.0414 -0.0335
2021-01-11  -0.0747  -0.1431  -0.1052  -0.0913  -0.1226  -0.2027 -0.1052
2021-01-12  -0.0390  -0.0345   0.0023   0.0176  -0.0111  -0.0400  0.0023
...             ...      ...      ...      ...      ...      ...     ...
2022-05-17   0.0189   0.0326   0.0298   0.0346   0.0436   0.0840  0.0298
2022-05-18  -0.0585  -0.0877  -0.0623  -0.0769  -0.0175  -0.1035 -0.0623
2022-05-19   0.0544   0.0531   0.0653   0.0361   0.0356   0.0884  0.0653
2022-05-20  -0.0376  -0.0304  -0.0161  -0.0250  -0.0322  -0.0498 -0.0161
2022-05-21   0.0142   0.0130   0.0364   0.0155   0.0501   0.0245  0.0364

[499 rows x 7 columns]

>>> atf.correlation # Correlation matrix
         BTCUSDT  ETHUSDT  BNBUSDT  XRPUSDT  TRXUSDT  LTCUSDT
BTCUSDT   1.0000   0.8184   0.6702   0.6158   0.6762   0.8066
ETHUSDT   0.8184   1.0000   0.6905   0.6319   0.6888   0.8259
BNBUSDT   0.6702   0.6905   1.0000   0.5819   0.6095   0.6878
XRPUSDT   0.6158   0.6319   0.5819   1.0000   0.6440   0.7064
TRXUSDT   0.6762   0.6888   0.6095   0.6440   1.0000   0.7311
LTCUSDT   0.8066   0.8259   0.6878   0.7064   0.7311   1.0000

>>> atf.stats # Various key statistics
         Return   Risk  Sharpe  Variance  Sys. Var.  Unsys. Var.   beta   CAPM   alpha
BTCUSDT -0.2094 0.7678 -0.3132    0.5895     0.6595      -0.0700 0.4015 0.5984 -0.8078
ETHUSDT  0.3532 0.9977  0.3230    0.9955     0.8830       0.1125 0.5375 0.7906 -0.4374
BNBUSDT  1.4442 1.2817  1.1026    1.6426     1.6426       0.0000 1.0000 1.4442  0.0000
XRPUSDT  0.1841 1.3398  0.1142    1.7952     0.9993       0.7959 0.6083 0.8907 -0.7066
TRXUSDT  0.6469 1.1672  0.5277    1.3624     0.9118       0.4506 0.5551 0.8154 -0.1685
LTCUSDT -0.6435 1.1357 -0.5939    1.2899     1.0011       0.2888 0.6095 0.8923 -1.5358
TP       1.4442 1.2817  1.1026    1.6426     1.6426       0.0000 1.0000 1.4442  0.0000
```
## Development

Run:
```sh
cd atf
pip install .[dev]
```

## Project 

https://github.com/streetyoga/atf

## License

[MIT](LICENSE.txt)
