# Black-Scholes Option Pricing Model

A Python implementation of the Black-Scholes model for European option pricing, Greeks calculation, and implied volatility estimation.

## Features

- **Option Pricing** — Computes European call and put prices using the Black-Scholes formula
- **Greeks** — Calculates Delta, Gamma, Vega, and Rho
- **Implied Volatility** — Estimates implied volatility from market prices using Newton's method
- **Visualization** — Plots call and put prices across a range of spot prices

## Requirements

- Python 3.11+
- NumPy
- SciPy
- Matplotlib

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install numpy scipy matplotlib
```

## Usage

```bash
python black_scholes.py --S 100 --K 105 --T 1 --r 0.05 --sigma 0.2
```

### Parameters

| Flag      | Description              |
|-----------|--------------------------|
| `--S`     | Current stock price      |
| `--K`     | Strike price             |
| `--T`     | Time to expiry (years)   |
| `--r`     | Risk-free interest rate  |
| `--sigma` | Volatility               |

### Example Output

```
--- Black-Scholes Option Pricer ---
Call Price:   $8.02
Put Price:    $8.90

--- Greeks ---
Delta (call): 0.4732
Delta (put):  -0.5268
Gamma:        0.0253
Vega:         19.6585
Rho (call):   42.1236

--- Implied Volatility ---
Implied Vol:  0.2000
```
