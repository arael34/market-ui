import os
import requests
import urllib.request

# dunno if these are needed yet
import pandas as pd
import numpy as np
from pandas_datareader import data as datareader
import datetime as dt
from datetime import date, timedelta

import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
pio.templates

import yfinance as yf

def main():
    sym = input("Enter stock symbol: ")

    start = dt.datetime(2022, 1, 1)
    now = dt.datetime.now()
    df = datareader.get_data_yahoo(sym, start, now)

    df.round(2)

    df = pd.DataFrame()
    sma10 ='sma10'
    sma80 ='sma80'
    #df[sma10]= df.iloc[:,4].rolling(window=10).mean()
    #df[sma80]= df.iloc[:,4].rolling(window=80).mean()
    df.round(2)

    fig = go.Figure(data=[go.Candlestick(x=df.index, name = 'Price',
                    open=df['Open'], high=df['High'], 
                    low=df['Low'], close=df['Close']),])
        #go.Scatter(x=data1.index, y=data1.sma10, name='SMA 10'),
        #go.Scatter(x=data1.index, y=data1.sma80,name='SMA 80')])

    for template in ["plotly_dark"]:
        fig.layout.font.family = 'Balto'
        fig.update_layout(template=template, 
            title="Historical Price and SME of '"+str(sym)+"' index")

    fig.show()

if __name__ == "__main__":
    main()
