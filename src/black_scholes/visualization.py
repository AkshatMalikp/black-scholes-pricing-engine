import numpy as np
import matplotlib.pyplot as plt

stock_prices = np.linspace(50, 150, 101)

print("Stock Prices:", stock_prices)


def plot_profit_curve(stock_prices, profits, strike_price, title):


    # Create figure
    plt.figure(figsize=(10, 6))

    # Plot stock prices against profits
    plt.plot(stock_prices, profits, label='Profit')

    # Draw horizontal zero-profit line
    plt.axhline(0, color='black', linestyle='--', linewidth=2)

    # Draw vertical strike-price line
    plt.axvline(strike_price, color='red', linestyle='-', linewidth=2)

    # Add axis labels
    ax = plt.gca()
    ax.set_xlabel('Stock Price at Expiration')

    # Add title
    ax.set_title(title)

    # Add legend
    plt.legend()

    # Display graph
    plt.show()
