# config.py

# Tickers to analyze (e.g., Apple, Goldman Sachs, S&P 500)
TICKERS = ['AAPL', 'GS', 'SPY']

# Weights must sum to 1.0
WEIGHTS = [0.4, 0.3, 0.3] 

# Time settings
START_DATE = '2020-01-01'
END_DATE = '2024-01-01'

# Simulation settings
SIM_DAYS = 252        # One trading year
NUM_SIMULATIONS = 5000
CONFIDENCE_LEVEL = 0.95
