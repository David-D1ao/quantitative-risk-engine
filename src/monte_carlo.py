import numpy as np
from scipy.stats import norm

class MonteCarloEngine:
    def __init__(self, initial_investment, drift, volatility, days, simulations):
        self.initial_inv = initial_investment
        self.drift = drift
        self.vol = volatility
        self.days = days
        self.sims = simulations

    def run_simulation(self):
        """
        Executes Geometric Brownian Motion (GBM).
        S_t = S_{t-1} * exp((mu - 0.5 * sigma^2)t + sigma * W_t)
        """
        # Create a matrix for daily returns: (Days, Simulations)
        # Generate random Z-scores from Normal Distribution
        Z = np.random.normal(0, 1, (self.days, self.sims))

        # Calculate daily returns using GBM formula
        # We use the daily drift and volatility derived from historical data
        daily_returns = np.exp((self.drift - 0.5 * self.vol**2) + self.vol * Z)

        # Create price matrix
        price_paths = np.zeros((self.days + 1, self.sims))
        price_paths[0] = self.initial_inv

        for t in range(1, self.days + 1):
            price_paths[t] = price_paths[t-1] * daily_returns[t-1]

        return price_paths

    def calculate_var(self, final_prices, confidence_level=0.95):
        """
        Calculates Value at Risk (VaR) and Conditional VaR (CVaR).
        """
        cutoff_percentile = (1 - confidence_level) * 100
        var_value = np.percentile(final_prices, cutoff_percentile)
        
        # Risk Amount = Initial - 5th Percentile outcome
        risk_amount = self.initial_inv - var_value
        
        return risk_amount, var_value
