# Vectorbt-MeanReversion-Strategy
Mean-Reversion Trading Strategy with Vectorbt: A Python Implementation on Apple Stock


Demonstrates a simple mean-reversion trading strategy using the `vectorbt` library in Python. The strategy involves generating buy and sell signals based on z-scores computed from the moving averages of a stock's closing prices. Below is a detailed description of the code:

1. **Importing Libraries:**
   - The necessary libraries are imported, including `yfinance`, `vectorbt`, `numpy`, and `pandas`.

2. **Fetching Stock Data:**
   - Stock data for Apple (AAPL) is downloaded using Yahoo finace API.
   - The closing prices are used to measure stock metrics and identify signals.

3. **Defining Parameters:**
   - Parameters for the moving averages and mean-reversion strategy are defined.
     - `short_window`: The window for the short-term moving average.
     - `long_window`: The window for the long-term moving average.
     - `entry_z_score`: The z-score threshold for generating buy signals.
     - `exit_z_score`: The z-score threshold for generating sell signals.

4. **Computing Moving Averages:**
   - Short-term and long-term moving averages are calculated using the `vbt.rolling_mean` method from the `vectorbt` library and stored in the `price_data` DataFrame.

5. **Computing Z-Scores:**
   - Z-scores are computed using the `vbt.zscore` method from the `vectorbt` library, providing a standardized measure of how far the closing prices deviate from the moving averages.

6. **Generating Entry and Exit Signals:**
   - Buy signals (`entry_signal`) are generated when the z-score is less than the specified entry threshold.
   - Sell signals (`exit_signal`) are generated when the z-score is greater than the specified exit threshold.

7. **Backtesting the Strategy:**
   - The backtest is performed using the `vbt.Portfolio.from_signals` method from the `vectorbt` library.
   - The initial cash is set to $1000, and transaction fees are considered in the simulation.

8. **Printing Results:**
   - The total returns of the strategy are printed using the `portfolio.total_profit()` method.
   - <img width="544" alt="image" src="https://github.com/keneccc/Vectorbt-MeanReversion-Strategy/assets/116320614/6791f60c-6356-4946-8da1-967a1d86f2bf">


   **Using Riskfolio for Portfolio Selection and Visualization**
Introduction
Create an optimal portfolio based on historical asset returns. 

Code Overview
Step 1: Data Preparation
Download Data: Retrieve historical price data for selected assets using Yahoo Finance (yfinance).
Calculate Returns: Compute percentage changes in asset prices to generate return data.

Step 2: **Portfolio Optimization**
Portfolio Object: Create a HCPortfolio object from Riskfolio using the returns data.
Optimization: Estimate optimal portfolio weights using the optimization() method with specific parameters:
Model: HERC (Hierarchical Equal Risk Contribution), HRP (Hierarchical Risk Parity), or other available models.
Correlation: Pearson correlation matrix for grouping assets in clusters.
Risk Measure: Variance (MV).
Risk-Free Rate: Set to 0 for this case.
Linkage Method: Ward method for building clusters.
Max K: Maximum number of clusters used in two different gap statistics.
Leaf Order: Consider the optimal order of leafs in the dendrogram.

Step 3: **Visualization Portfolio Weight Allocation**
Pie Chart: Use Riskfolio's plot_pie() function from PlotFunctions to visualize the composition of the optimized portfolio:
Display the pie chart illustrating the asset allocation based on calculated weights.
Set parameters such as title, other categories, color map, height, and width.
![image](https://github.com/keneccc/Vectorbt-MeanReversion-Strategy/assets/116320614/7b32167a-38e9-4476-a547-36342553d903)


Possible future changes
Customization: Modify parameters and functions to suit specific portfolio preferences and visualization requirements.
Documentation: Refer to Riskfolio's official documentation for detailed explanations of available functions, parameters, and usage examples.

Next steps will involve connection strategy to broker API and automating paper and live trading.




