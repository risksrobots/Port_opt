from inherited_classes.inh_getting_market_data import MoscowExchangeData

tickers = ['GMKN', 'SIBN', 'MTSS', 'POLY', 'HYDR', 'MOEX', 'VTBR', 'BANE',
           'SNGS', 'ETLN', 'ALRS', 'IRAO', 'LKOH', 'ROSN', 'SNGSP', 'SBER',
           'GAZP', 'NVTK', 'RUAL', 'RSTIP', 'TRNFP', 'SBERP', 'AFKS',
           'INTC-RM', 'POGR', 'MGNT', 'NMTP', 'MAGN', 'AFLT', 'QIWI', 'FXRL',
           'FB-RM', 'TATN', 'NKNCP', 'PLZL', 'BA-RM', 'NLMK', 'CHMF', 'RASP',
           'MSNG', 'YNDX', 'FEES', 'FIVE', 'KRKNP', 'LSNGP', 'UPRO', 'DSKY',
           'AGRO', 'BANEP', 'MAIL', 'LSRG', 'ENRU', 'RTKM', 'AKRN', 'TATNP',
           'TCSG', 'CNYRUB_TOM', 'XOM-RM', 'RTKMP', 'AAPL-RM', 'NVDA-RM',
           'VTBX', 'OGKB', 'LNTA', 'RUSB', 'TRUR', 'BSPB', 'LIFE', 'FXGD',
           'SBSP', 'FXKZ', 'TGKA', 'LNZL', 'PHOR', 'FXIT', 'SBMX', 'RSTI',
           'MRKP', 'SBRB', 'MTLR', 'SBGB', 'FXRU', 'SFIN', 'FXUS', 'MVID',
           'MU-RM', 'FXRW', 'MTLRP', 'APTK', 'PIKK', 'FXTB', 'CBOM', 'PFE-RM',
           'T-RM', 'FXWO', 'EUR_RUB__TOM', 'FXMM', 'FXDE', 'TGKB', 'SELG',
           'VTBB', 'FXRB', 'VTBM', 'FXCN', 'AMD-RM', 'VTBG', 'RUSE', 'VTBE',
           'VTBA', 'MA-RM', 'ATVI-RM', 'SBCB', 'MSFT-RM', 'NFLX-RM',
           'AMZN-RM', 'GOOG-RM', 'MTEK', 'DIS-RM', 'EUR_RUB__TOD', 'VTBH',
           'TRMK', 'SCIP', 'RCMX', 'V-RM', 'TWTR-RM', 'ABBV-RM', 'PYPL-RM',
           'BABA-RM', 'BIIB-RM', 'F-RM', 'CSCO-RM', 'MCD-RM', 'EA-RM',
           'AAL-RM', 'FDX-RM', 'GLDRUB_TOM', 'NEM-RM', 'WMT-RM', 'TSLA-RM',
           'BIDU-RM', 'BMY-RM', 'QCOM-RM', 'CRM-RM', 'HPQ-RM', 'AVGO-RM',
           'ADBE-RM']

dict_urls = {'foreign_shares': 'https://iss.moex.com/iss/history/engines/stock/markets/foreignshares/securities/',
             'russian_shares': 'http://iss.moex.com/iss/history/engines/stock/markets/shares/boards/tqbr/securities/'}

start_date = '2020-09-01'
finish_date = '2020-12-31'

market_data_getter = MoscowExchangeData(dict_urls, tickers, start_date, finish_date)
print(market_data_getter.get_data())
