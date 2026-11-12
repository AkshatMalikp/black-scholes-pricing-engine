
# Black-Scholes Pricing Engine

A Python-based quantitative finance project implementing the Black-Scholes-Merton option pricing model from scratch.

## Project Objectives

- Understand European call and put options.
- Implement the Black-Scholes pricing formula.
- Calculate option Greeks.
- Estimate implied volatility.
- Simulate stock price paths using Geometric Brownian Motion.
- Compare analytical pricing with Monte Carlo simulation.
- Visualize option prices and volatility surfaces.

## Mathematical Foundation

The Black-Scholes model calculates the theoretical price of European options.

Call option:

C = S * N(d1) - K * exp(-rT) * N(d2)

Put option:

P = K * exp(-rT) * N(-d2) - S * N(-d1)

Where:
- S: Current underlying asset price
- K: Strike price
- T: Time to expiration
- r: Risk-free interest rate
- sigma: Volatility
- N(): Standard normal cumulative distribution function

## Technology Stack

- Python
- NumPy
- SciPy
- Pandas
- Matplotlib
- pytest
- Streamlit

## Project Structure

```text
src/          Core pricing engine
tests/        Unit tests
notebooks/    Mathematical experiments
docs/         Documentation
```

## Development Roadmap

1. Options fundamentals
2. Black-Scholes implementation
3. Option Greeks
4. Implied volatility
5. Monte Carlo simulation
6. Volatility visualization
7. Interactive dashboard

## Author

Akshat Malik
