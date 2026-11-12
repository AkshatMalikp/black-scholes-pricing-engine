import numpy as np

from black_scholes.payoffs import long_call_profit
from black_scholes.visualization import plot_profit_curve

strike_price = 100
premium = 5

stock_prices = np.linspace(50, 150, 101)

profits = [
    long_call_profit(price, strike_price, premium)
    for price in stock_prices
]

plot_profit_curve(
    stock_prices,
    profits,
    strike_price,
    "Long Call Profit Diagram"
)