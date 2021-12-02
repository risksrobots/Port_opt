from getting_market_data import AbstractGetPreprocMarketData
import pandas as pd
from urllib.request import urlopen
import urllib.request


class MoscowExchangeData(AbstractGetPreprocMarketData):
    """
    A class used to represent a way of getting market data
    from Moscow Exchange

    Attributes
    ----------
    (static) required_attributes : list
      a dict where keys are attributes' names,
      values are required types
      of required attributes
    (static) dict_urls_keys : dict
      a container with keys required for dict_urls
    dict_urls : dict
      a dict where keys are identificators of URLs, values are URLs
      for grabbing market data
    tickers : list
      a list of short identificators of market assets
    start_date : str
      a string in format 'YYYY-MM-DD' for URL to get market data
      from this date
    finish_date : str
      a string in format 'YYYY-MM-DD' for URL to get market data
      until this date

    Methods
    ----------
    get_data(self) -> dict
      Returns a dict where keys are assets' tickers,
      values are time-series dataframes
      with 2 following columns:
        tradedate : datetime64[ns],
        close : float64.
    preprocess_datа(dict_market_prices: dict) -> dict
      Returns a dict where keys are assets' tickers,
      values are preprocessed time-series dataframes
    main(self) -> dict
      A class method used for getting and preprocessing market data.
      Returns a market prices' dict.
    """
    required_attributes = {
        'dict_urls': dict,
        'tickers': list,
        'start_date': str,
        'finish_date': str,
    }

    dict_urls_keys = ['foreign_shares', 'russian_shares']

    def get_data(self):
        """Returns a dict where keys are assets' tickers,
        values are time-series dataframes """

        dict_market_prices = dict()
        for ticker in self.tickers:
            if '-' in ticker:
                url0 = self.dict_urls['foreign_shares'] + str(ticker) \
                    + '.csv' + '?from=' + self.start_date + '&till=' \
                    + self.finish_date + '&start={}'
                slice_end = -8
            else:
                url0 = self.dict_urls['russian_shares'] + str(ticker) \
                    + '.csv' + '?from=' + self.start_date + '&till=' \
                    + self.finish_date + '&start={}'
                slice_end = -2

            step = 0  # iterator pointed from which row data is grabbed

            while True:
                url = url0.format(step)
                response = urllib.request.urlopen(url)

                df_list = list()
                for i in response.readlines()[2:slice_end]:
                    df_list.append(str(i)[2:-3].split(';'))

                df_loc = pd.DataFrame(df_list[1:], columns=df_list[0])

                if len(df_loc) == 0:
                    break

                if step == 0:
                    df = df_loc
                else:
                    df = df.append(df_loc)

                step += 100

            if len(df) != 0:
                dict_market_prices[ticker] = df

        return dict_market_prices
