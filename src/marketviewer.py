import os
from tkinter import Y
import requests
import urllib.request

# dunno if these are needed yet
import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
import datetime as dt
from datetime import date, timedelta

import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
pio.templates

import yfinance as yf

def main():
    yf.pdr_override()

    sym = input("Enter stock symbol: ")

    start = dt.datetime(2022, 1, 1)
    now = dt.datetime.now()
    df = pdr.get_data_yahoo(sym, start, now)

    df.round(3)

    data = pd.DataFrame()
    data['average10']= df.iloc[:,4].rolling(window=10).mean()
    data['average80']= df.iloc[:,4].rolling(window=80).mean()
    data.round(2)

    fig = go.Figure(data=[go.Candlestick(x=df.index, name = 'Price',
                    open=df['Open'], high=df['High'], 
                    low=df['Low'], close=df['Close']),
        go.Scatter(x = data.index, y = data.average10, name = '10 day moving average'),
        go.Scatter(x = data.index, y = data.average80, name = '80 day moving average')])

    """ for template in ["plotly_dark"]:
        fig.layout.font.family = 'Balto'
        fig.update_layout(template=template, 
            title="Historical Price and SME of '"+str(sym)+"' index") """

    fig.show()

if __name__ == "__main__":
    main()
