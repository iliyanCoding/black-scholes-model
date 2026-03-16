import argparse
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt


def black_scholes(S, K, T, r, sigma):
    d1, d2 = compute_d1_d2(S, K, T, r, sigma)
    # calculate call and put price
    call = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    put = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

    return call, put


def compute_d1_d2(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + (sigma**2 / 2)) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    return d1, d2


def greeks(S, K, T, r, sigma):
    d1, d2 = compute_d1_d2(S, K, T, r, sigma)

    delta_call = norm.cdf(d1)
    delta_put = delta_call - 1
    gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
    vega = S * norm.pdf(d1) * np.sqrt(T)
    rho_call = K * T * np.exp(-r * T) * norm.cdf(d2)

    return delta_call, delta_put, gamma, vega, rho_call


def plot_option(K, T, r, sigma):
    spot_prices = np.linspace(50, 200, 300)
    call_prices, put_prices = black_scholes(spot_prices, K, T, r, sigma)
    plt.figure(figsize=(10, 6))
    plt.plot(spot_prices, call_prices, label="Call prices")
    plt.plot(spot_prices, put_prices, label="Put prices")
    plt.axvline(x=K, linestyle="--", label="Strike")
    plt.xlabel("Stock prices")
    plt.ylabel("Option price")
    plt.title("Black-Scholes model")
    plt.legend()
    plt.grid(True)
    plt.show()


def implied_volatility(market_price, S, K, T, r, option_type="call"):
    sigma = 0.2  # this is the initial guess
    tolerance = 1e-6
    max_iterations = 1000

    for _ in range(max_iterations):
        call, put = black_scholes(S, K, T, r, sigma)
        price = call if option_type == "call" else put
        error = price - market_price

        if abs(error) < tolerance:
            return sigma

        vega = greeks(S, K, T, r, sigma)[3]

        sigma = sigma - (price - market_price) / vega

    return sigma


def plot_vol_smile(S, K, T, r, sigma):
    strikes = np.linspace(50, 150, 300)
    market_sigmas = [add_vol_smile(strike, S, sigma) for strike in strikes]
    call_prices = [
        black_scholes(S, strike, T, r, ms)[0]
        for strike, ms in zip(strikes, market_sigmas)
    ]
    plt.figure(figsize=(10, 6))
    impl_vol = [
        implied_volatility(price, S, strike, T, r)
        for price, strike in zip(call_prices, strikes)
    ]
    plt.plot(strikes, impl_vol, label="Implied volatility")
    plt.xlabel("Strike price")
    plt.ylabel("Implied volatility")
    plt.title("Volatility Smile")
    plt.legend()
    plt.grid(True)
    plt.show()


def add_vol_smile(strike, S, base_sigma):
    moneyness = abs(np.log(S / strike))
    smile_sigma = base_sigma + 0.1 * moneyness**2
    return smile_sigma


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Black-Scholes Option Pricer")
    parser.add_argument("--S", type=float, required=True, help="Stock price")
    parser.add_argument("--K", type=float, required=True, help="Strike price")
    parser.add_argument(
        "--T", type=float, required=True, help="Time to expiry in years"
    )
    parser.add_argument("--r", type=float, required=True, help="Risk-free rate")
    parser.add_argument("--sigma", type=float, required=True, help="Volatility")
    args = parser.parse_args()

    call, put = black_scholes(args.S, args.K, args.T, args.r, args.sigma)
    delta_call, delta_put, gamma, vega, rho_call = greeks(
        args.S, args.K, args.T, args.r, args.sigma
    )

    print(f"\n--- Black-Scholes Option Pricer ---")
    print(f"Call Price:   ${call:.2f}")
    print(f"Put Price:    ${put:.2f}")
    print(f"\n--- Greeks ---")
    print(f"Delta (call): {delta_call:.4f}")
    print(f"Delta (put):  {delta_put:.4f}")
    print(f"Gamma:        {gamma:.4f}")
    print(f"Vega:         {vega:.4f}")
    print(f"Rho (call):   {rho_call:.4f}")
    print(f"\n--- Implied Volatility ---")
    iv = implied_volatility(call, args.S, args.K, args.T, args.r, option_type="call")
    print(f"Implied Vol:  {iv:.4f}")
    plot_option(args.K, args.T, args.r, args.sigma)
    plot_vol_smile(args.S, args.K, args.T, args.r, args.sigma)
