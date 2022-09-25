import streamlit as sl

import pandas as pd
from pandas_datareader import data as pdr
import datetime as dt

import plotly.graph_objects as go
import yfinance as yf
class App:
    def __init__(self):
        yf.pdr_override()

        self.sym = sl.text_input("Stock Symbol", value="", type="default", label_visibility="visible")
        sl.button("Show", on_click = self.graph)

    def graph(self):
        if self.sym == "":
            return

        start = dt.datetime(2022, 1, 1)
        now = dt.datetime.now()
        df = pdr.get_data_yahoo(self.sym, start, now)

        df.round(2)

        data = pd.DataFrame()
        data['average10']= df.iloc[:,4].rolling(window=10).mean()
        #data['average80']= df.iloc[:,4].rolling(window=80).mean()
        data.round(2)

        fig = go.Figure(data=[go.Candlestick(x=df.index, name = 'Price',
                        open=df['Open'], high=df['High'], 
                        low=df['Low'], close=df['Close']),
            go.Scatter(x = data.index, y = data.average10, name = '10 day moving average')])
            #go.Scatter(x = data.index, y = data.average80, name = '80 day moving average')])

        sl.plotly_chart(fig)

def main():
    app = App()
    
if __name__ == "__main__":
    main()