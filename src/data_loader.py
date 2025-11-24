import yfinance as yf
import pandas as pd
import numpy as np

class DataLoader:
    def __init__(self, tickers, start_date, end_date):
        self.tickers = tickers
        self.start_date = start_date
        self.end_date = end_date

    def get_data(self):
        """
        Fetches adjusted close prices and calculates daily log returns.
        """
        print(f"Fetching data for: {self.tickers}...")
        data = yf.download(self.tickers, start=self.start_date, end=self.end_date)['Adj Close']
        
        # Calculate Log Returns (mathematically superior for aggregation)
        log_returns = np.log(data / data.shift(1)).dropna()
        
        return data, log_returns

    def get_portfolio_statistics(self, log_returns, weights):
        """
        Calculates the portfolio's historical drift and volatility.
        """
        weights = np.array(weights)
        
        # Expected Annual Return (Drift) based on historical mean
        # 252 trading days in a year
        avg_daily_return = np.sum(log_returns.mean() * weights)
        drift = avg_daily_return # Daily drift

        # Portfolio Volatility (Standard Deviation)
        # Uses Covariance Matrix to account for correlation between assets
        cov_matrix = log_returns.cov()
        variance = np.dot(weights.T, np.dot(cov_matrix, weights))
        daily_volatility = np.sqrt(variance)

        return drift, daily_volatility
