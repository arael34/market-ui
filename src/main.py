from tkinter import *
from tkinter import ttk

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

class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()
        self.title("Python Tkinter")
        self.geometry("600x600")
        self.resizable(0, 0)
        self.stock_text = ttk.Entry(self)
        self.stock_text.place(x = 200, y = 100)
        ttk.Button(self, text = "View", command = self.view).place(x = 400, y = 100)

    def view(self):
        text = self.stock_text.get()
        if text == '':
            return
        sym = text
        start = dt.datetime(2022, 1, 1)
        now = dt.datetime.now()
        df = pdr.get_data_yahoo(sym, start, now)

        df.round(3)

        data = pd.DataFrame()
        sma10 ='sma10'
        sma80 ='sma80'
        data[sma10]= df.iloc[:,4].rolling(window=10).mean()
        data[sma80]= df.iloc[:,4].rolling(window=80).mean()
        data.round(2)

        fig = go.Figure(data=[go.Candlestick(x=df.index, name = 'Price',
                        open=df['Open'], high=df['High'], 
                        low=df['Low'], close=df['Close']),
            go.Scatter(x=data.index, y=data.sma10, name='SMA 10'),
            go.Scatter(x=data.index, y=data.sma80,name='SMA 80')])

        """ for template in ["plotly_dark"]:
            fig.layout.font.family = 'Balto'
            fig.update_layout(template=template, 
                title="Historical Price and SME of '"+str(sym)+"' index") """

        fig.show()

def main():
    root = Root()
    root.mainloop()

if __name__ == "__main__":
    main()

"""
TODO
make resizable, learn how to use grid/pack for buttons and such

default screen
options - create new folder, view quotes, view watchlists

libraries - tkinter, market api, statplots, probably math

how much more volatile than the market? give an basis

need a database at some point
"""