
import matplotlib.pyplot as plt
import numpy as np

class RiskVisualizer:
    @staticmethod
    def plot_simulation(price_paths):
        plt.figure(figsize=(10, 6))
        plt.plot(price_paths[:, :50]) # Only plot first 50 sims to avoid clutter
        plt.title(f'Monte Carlo Simulation: Projected Portfolio Paths')
        plt.xlabel('Trading Days')
        plt.ylabel('Portfolio Value ($)')
        plt.grid(True, alpha=0.3)
        plt.show()

    @staticmethod
    def plot_distribution(final_prices, var_level):
        plt.figure(figsize=(10, 6))
        plt.hist(final_prices, bins=50, alpha=0.7, color='blue', edgecolor='black')
        plt.axvline(var_level, color='r', linestyle='dashed', linewidth=2, label=f'VaR Threshold')
        plt.title('Distribution of Final Portfolio Values')
        plt.xlabel('Value ($)')
        plt.ylabel('Frequency')
        plt.legend()
        plt.show()
