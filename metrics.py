import yfinance as yf
import vectorbt as vbt
import numpy as np
import pandas as pd

# Fetch Apple stock data
apple_data = yf.download('AAPL', start='2023-01-01', end='2023-12-31')

# Use the closing price for simplicity
price_data = pd.DataFrame({'price': apple_data['Close']})

# Define moving average and mean-reversion parameters
short_window = 10
long_window = 50
entry_z_score = -2.0
exit_z_score = 0.0

# Compute moving averages using vectorbt
price_data['short_ma'] = price_data['price'].vbt.rolling_mean(window=short_window)
price_data['long_ma'] = price_data['price'].vbt.rolling_mean(window=long_window)

# Compute z-scores using vectorbt
z_scores = price_data['price'].vbt.zscore()
price_data['z_score'] = z_scores

entry_signal = price_data['z_score'] < entry_z_score
exit_signal = price_data['z_score'] > exit_z_score

# Backtest the strategy
portfolio = vbt.Portfolio.from_signals(
    price_data['price'],
    entries=entry_signal,
    exits=exit_signal,
    init_cash=1000,
    fees=0.001
)

# Print the returns
print("Total Returns: ", portfolio.total_profit())
