import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
from controllers.viewer import view

def graph_init(app, text):
    fig = view(text)
    dash_app = dash.Dash(server=app, name="Dashboard", url_base_pathname="/view/")
    dash_app.layout = html.Div(
        children=[
            dcc.Graph(
                id="fig",
                figure=fig,
            ),
        ]
    )

    return dash_app