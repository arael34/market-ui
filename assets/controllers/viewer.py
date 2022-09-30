import pandas as pd
from pandas_datareader import data as pdr
import datetime as dt

import plotly.graph_objects as go
import plotly.io as pio
pio.templates

import yfinance as yf

"""
main stock view function. data is grabbed from yahoo finance
"""
def view_f(sym):
    yf.pdr_override()
    start = dt.datetime(2022, 1, 1)
    now = dt.datetime.now()
    df = pdr.get_data_yahoo(sym, start, now)

    df.round(2)

    data = pd.DataFrame()
    data['average10']= df.iloc[:,4].rolling(window=10).mean() # SMA 10
    data['average80']= df.iloc[:,4].rolling(window=80).mean() #SMA 80
    data.round(2)
    # plotly fig
    fig = go.Figure(data=[go.Candlestick(x=df.index, name = 'Price',
                    open=df['Open'], high=df['High'], 
                    low=df['Low'], close=df['Close']),
        go.Scatter(x = data.index, y = data.average10, name = '10 day moving average'),
        go.Scatter(x = data.index, y = data.average80, name = '80 day moving average')])

    return fig
