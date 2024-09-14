# region imports
from AlgorithmImports import *
from tensorflow.keras.models import Sequential
import json
# endregion

class CalculatingBrownTapir(QCAlgorithm):

    def initialize(self):
        self.set_start_date(2018, 1, 1)
        self.set_end_date(2020, 1, 1)

        # fetch model
        model_key = 'bitcoin_price_predictor'
        if self.ObjectStore.ContainsKey(model_key):
            model_str = self.ObjectStore.Read(model_key)
            config = json.loads(model_str)['config']
            self.model = Sequential.from_config(config)

        self.set_brokerage_model(BrokerageName.BITFINEX, AccountType.MARGIN)
        self.set_cash(100000)

        self.symbol = self.add_crypto("BTCUSD", Resolution.DAILY).symbol
        self.set_benchmark(self.symbol)

    def on_data(self, data: Slice):

        # convert model output [0, 1] to the range [-1, 1]
        # so if the model returns 0.5, this becomes 0 and algorithm doesn't take a position
        # otherwise positive->long position, negative->short position
        result = (2 * self.GetPrediction()) - 1
        self.set_holdings(self.symbol, result)
        
    

    def GetPrediction(self):
        # feed model data from the past 30 days, return output
        df = self.History(self.symbol, 40).loc[self.symbol]
        df_change = df[["open", "high", "low", "close", "volume"]].pct_change().dropna()
        model_input = []
        for index, row in df_change.tail(30).iterrows():
            model_input.append(np.array(row))
        model_input = np.array([model_input])
        
        # outputs a number between 0 and 1
        # 0 indicating a downtrend prediction and 1 indicating an uptrend
        return self.model.predict(model_input)[0][0]
