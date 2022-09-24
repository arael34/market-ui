from flask import Flask, request, render_template

import pandas as pd
from pandas_datareader import data as pdr
import datetime as dt
import plotly.graph_objects as go
import plotly.io as pio
pio.templates

import yfinance as yf

def market_viewer(text):
    yf.pdr_override()

    start = dt.datetime(2022, 1, 1)
    now = dt.datetime.now()
    df = pdr.get_data_yahoo(text, start, now)

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

def main():
    app = Flask(__name__)
    @app.route('/')
    def home():
        return render_template("temp.html")
    
    @app.route('/', methods=['POST'])
    def my_form_post():
        text = request.form['text']
        return market_viewer(text)

    app.run(host='0.0.0.0', port=81)

if __name__ == "__main__":
    main()
