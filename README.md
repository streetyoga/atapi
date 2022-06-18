# Algorithmic Trading API

Backtest, forward tests and deploy trading algorithms and strategies on binance spot, futures and nft markets and other cryptocurrency exchanges, including arbitrage.

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
python -m atapi
```
```sh
Welcome to the Algorithmic Trading API. Type help/? for commands.

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
atf🖖 help stats
Return, risk, sharpe, variance, systematic variance,
unsystematic variance, beta, CAPM, alpha.
```
```sh
atf🖖 returns
==========  =========  =========  =========  =========  =========  =========  =======
Date          BTCUSDT    ETHUSDT    BNBUSDT    XRPUSDT    TRXUSDT    LTCUSDT       TP
==========  =========  =========  =========  =========  =========  =========  =======
2021-02-05     0.0360     0.0746     0.1905     0.0150     0.0906     0.0665   0.1905
2021-02-06     0.0231    -0.0252     0.0731    -0.0204    -0.0328     0.0033   0.0731
2021-02-07    -0.0100    -0.0394    -0.0635    -0.0571     0.0253    -0.0314  -0.0635
2021-02-08     0.1784     0.0825     0.1553     0.0748     0.1166     0.1040   0.1553
2021-02-09     0.0010     0.0108     0.2961     0.0547     0.1311     0.0815   0.2961
```
```sh
atf🖖 correlation
=======  =========  =========  =========  =========  =========  =========  ======
..         BTCUSDT    ETHUSDT    BNBUSDT    XRPUSDT    TRXUSDT    LTCUSDT      TP
=======  =========  =========  =========  =========  =========  =========  ======
BTCUSDT     1.0000     0.8274     0.6859     0.6737     0.6815     0.7988  0.6859
ETHUSDT     0.8274     1.0000     0.7152     0.7067     0.6929     0.8277  0.7152
BNBUSDT     0.6859     0.7152     1.0000     0.6416     0.6131     0.7027  1.0000
XRPUSDT     0.6737     0.7067     0.6416     1.0000     0.7020     0.7754  0.6416
TRXUSDT     0.6815     0.6929     0.6131     0.7020     1.0000     0.7192  0.6131
LTCUSDT     0.7988     0.8277     0.7027     0.7754     0.7192     1.0000  0.7027
TP          0.6859     0.7152     1.0000     0.6416     0.6131     0.7027  1.0000
=======  =========  =========  =========  =========  =========  =========  ======
```
```sh
atf🖖 stats
=======  ========  ======  ========  ==========  ===========  =============  ======  ======  =======    
..         Return    Risk    Sharpe    Variance    Sys. Var.    Unsys. Var.    beta    CAPM    alpha    
=======  ========  ======  ========  ==========  ===========  =============  ======  ======  =======    
BTCUSDT   -0.4338  0.7622   -0.6097      0.5810       0.6677        -0.0867  0.4093  0.4185  -0.8523    
ETHUSDT   -0.2869  0.9724   -0.3270      0.9456       0.8883         0.0573  0.5446  0.5465  -0.8335    
BNBUSDT    0.9777  1.2772    0.7412      1.6312       1.6312         0.0000  1.0000  0.9777   0.0000    
XRPUSDT   -0.2421  1.2527   -0.2180      1.5692       1.0264         0.5427  0.6292  0.6267  -0.8688    
TRXUSDT    0.4359  1.1706    0.3459      1.3703       0.9167         0.4536  0.5620  0.5630  -0.1271    
LTCUSDT   -0.8158  1.1224   -0.7545      1.2597       1.0073         0.2524  0.6175  0.6156  -1.4315    
TP         0.9777  1.2772    0.7412      1.6312       1.6312         0.0000  1.0000  0.9777   0.0000    
=======  ========  ======  ========  ==========  ===========  =============  ======  ======  =======  
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
