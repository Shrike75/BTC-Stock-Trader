# Crypto-Neural-Net

Backtest results are in **Strategy_Report**

Code logic is in **BTC_ML_Pred_16/**

**research.ipynb:**
- Fetch historical market data using QuantConnect API
- Train neural network
  -  Predict binary price movement given most recent 30-day data
- Save model to the QC Book


**main.py:**
- Fetch trained model
- On a stock change, input current data to model
- Set portfolio holdings based on model's confidence in a binary movement

Generates roughly **10%** returns from 2018 to 2020, even though Bitcoin's stock fell during this period.

Quite strong given Bitcoin's price volatility. Able to predict when to go short fairly well.

Still room to improve, particularly in portfolio construction. Low Sharpe Ratio suggests intra-day volatility even though it is generally stable long-term. Taking a more rounded, risk-adjusted approach to setting BTC holdings given the model output would be beneficial.
