from datetime import date

import pandas as pd
import yfinance as yf

TICKERS = ['VFINX', 'VINEX', 'FDFAX', 'SCZ', 'SPY','VSS', 'SCHA', 'SCHH', 'SCHD']

PERIODS = {'1M': 21,
           '3M': 21 * 3,
           '6M': 21 * 6, }


def get_performance(run_date, tickers):
    hist = tickers.history('1y')
    ref_date = pd.Timestamp(run_date)
    ref_price = hist.Close.loc[ref_date]

    performance = {}
    for period, offset in PERIODS.items():
        p_date = hist.index.values[-1 * offset]
        p_price = hist.Close.loc[p_date]

        performance[period] = (ref_price - p_price) / p_price * 100

    return pd.DataFrame(performance)


def avg(run_date=None, ):
    run_date = run_date or date.today()
    tickers = yf.Tickers(TICKERS)
    perf = get_performance(run_date, tickers).transpose().mean()
    return perf
