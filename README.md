# Crypto-Neural-Net

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

Gives about **10%** returns from 2018 to 2020. 

Quite strong given Bitcoin's price volatility. Limited bias since in this time period, Bitcoin's stock fell.
