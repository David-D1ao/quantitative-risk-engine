import config
from src.data_loader import DataLoader
from src.monte_carlo import MonteCarloEngine
from src.visualizer import RiskVisualizer

def main():
    print("--- QUANTITATIVE RISK ENGINE INITIALIZED ---")
    
    # 1. Load Data
    loader = DataLoader(config.TICKERS, config.START_DATE, config.END_DATE)
    _, log_returns = loader.get_data()
    
    # 2. Calculate Portfolio Metrics
    drift, vol = loader.get_portfolio_statistics(log_returns, config.WEIGHTS)
    print(f"Annualized Volatility: {vol * (252**0.5):.2%}")
    
    # 3. Run Monte Carlo Simulation
    initial_investment = 100000 # $100k portfolio
    engine = MonteCarloEngine(initial_investment, drift, vol, config.SIM_DAYS, config.NUM_SIMULATIONS)
    price_paths = engine.run_simulation()
    
    # 4. Calculate Risk
    risk_amt, worst_case = engine.calculate_var(price_paths[-1], config.CONFIDENCE_LEVEL)
    
    print(f"\n--- RESULTS ---")
    print(f"Initial Investment: ${initial_investment:,.2f}")
    print(f"Value at Risk (95%): ${risk_amt:,.2f}")
    print(f"This means with 95% confidence, you will not lose more than ${risk_amt:,.2f} in one year.")
    
    # 5. Visualize
    RiskVisualizer.plot_simulation(price_paths)
    RiskVisualizer.plot_distribution(price_paths[-1], worst_case)

if __name__ == "__main__":
    main()
