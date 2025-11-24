# quantitative-risk-engine
Monte Carlo Risk Engine (simulating the future price of stock portfolio 1,000 times to calculate VaR

Repository Structure
quantitative-risk-engine/
│
├── data/                   # Folder for caching CSVs (optional)
├── src/                    # Source code
│   ├── __init__.py
│   ├── data_loader.py      # Pulls real stock data (Yahoo Finance)
│   ├── monte_carlo.py      # The math logic (Geometric Brownian Motion)
│   └── visualizer.py       # Plots the results
│
├── main.py                 # The entry point (run this file)
├── config.py               # Settings (tickers, time horizon)
├── requirements.txt        # Dependencies
└── README.md               # The "Sales Pitch" (CRITICAL)
