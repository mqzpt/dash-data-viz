# Helloooooo

import dash
from dash import html
from dash import dcc
import plotly.express as px
import pandas as pd

# Read some test data
data = pd.read_csv("precious_metals_prices_2018_2021.csv", usecols=['DateTime', 'Gold'])

# Make a plotly figure for use by dcc.Graph()
fig = px.line(
    data, 
    x='DateTime', 
    y=['Gold'], 
    title='Precious Metal Prices 2018-2021', 
    color_discrete_map={'Gold':'gold'}
    )

fig.update_layout(
    template='plotly_dark',
    xaxis_title='Date',
    yaxis_title='Price (USD/oz)',
    font=dict(
        family= 'Verdana, sans-serif',
        size = 18,
        color = 'white'
    )
)
app = dash.Dash(__name__)
app.title = 'Precious Metals Prices 2018-2021'

app.layout = html.Div(
    id="app-container",
    children=[
        html.H1("Precious Metals Prices 2018-2021"),
        html.P("Results are in USD/oz"), 
        dcc.Graph(figure=fig)
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
