# Black-Scholes Option Pricing Model

A Python implementation of the Black-Scholes model for European option pricing, Greeks calculation, implied volatility estimation, and volatility smile visualization.

## Features

- **Option Pricing** — Computes European call and put prices using the Black-Scholes formula
- **Greeks** — Calculates Delta, Gamma, Vega, Theta, and Rho
- **Implied Volatility** — Estimates implied volatility from market prices using Newton's method
- **Volatility Smile** — Simulates and plots the implied volatility smile across strike prices
- **Visualization** — Plots call and put prices across a range of spot prices
- **Input Validation** — Validates all inputs with descriptive error messages

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
Theta (call): -0.0147

--- Implied Volatility ---
Implied Vol:  0.2000
```

Two plots are also displayed:
1. **Option prices** — Call and put prices vs. spot price, with strike price marked
2. **Volatility smile** — Implied volatility vs. strike price, showing the characteristic smile shape

## How It Works

The model prices European options using the Black-Scholes formula:

$$C = S \cdot N(d_1) - K e^{-rT} \cdot N(d_2)$$

$$P = K e^{-rT} \cdot N(-d_2) - S \cdot N(-d_1)$$

where:

$$d_1 = \frac{\ln(S/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}}, \quad d_2 = d_1 - \sigma\sqrt{T}$$

The volatility smile is simulated by adding a moneyness-dependent adjustment to the base volatility, then recovering implied volatilities via Newton's method.
