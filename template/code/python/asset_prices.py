import pandas as pd
import pandas_datareader as web
import time
import os

class asset_prices:

    def __init__(self, symbol='SPY'):
        # inputs
        self.symbol = symbol
        self.df = pd.DataFrame()

        # outputs
        self.train_df = pd.DataFrame()
        self.test_df = pd.DataFrame()

        # set root directory
        os.chdir("../../")
        print("root directory = %s " % os.getcwd())

        return

    def load_data(self):
        """ Load data from extracts using pandas.
        """
        print("Downloading %s file from web" % self.symbol)
        df = web.DataReader(name=self.symbol, data_source='yahoo', start="1/1/2006")
        df.to_csv("input/" + self.symbol + ".csv", sep=',', index=True)
        return

    def clean_data(self):
        """ Clean data from extracts using pandas.
        """

        return

    def join_data(self):
        """ merge multiple datasets
        """

        return

    def transform_data(self):
        """ Engineer features.
        """

        return

    def visualize_data(self):
        """ Visualize data, e.g., candle chart.
        """

        return

    def summarize_data(self):
        """ Visualize data, e.g., candle chart.
        """

        return

    def train_baseline_model(self):
        """ Build a baseline training model with train data in self.train_df
        """

        return

    def evaluate_baseline_model(self):
        """ Evalute your model with test data in self.test_df
        """

        return


    def train_model(self):
        """ Build a training model with train data in self.train_df
        """

        return

    def evaluate_model(self):
        """ Evalute your model with test data in self.test_df
        """

        return

    def main(self):
        """ Driver function that calls the other functions
        """

        t0_clock = time.process_time()
        # load, clean, and enrich data
        self.load_data()
        self.clean_data()
        self.join_data()
        self.transform_data()

        # explore data
        self.visualize_data()
        self.summarize_data()

        #  training and evalutoin of models
        self.train_baseline_model()
        self.evaluate_baseline_model()
        self.train_model()
        self.evaluate_model()

        t1_clock = time.process_time()
        print("\nTotal CPU time = %.1f minutes." % round((t1_clock - t0_clock) / 60, 1))


if __name__ == '__main__':
    ap = asset_prices()
    ap.main()
    import doctest

    doctest.testmod()
