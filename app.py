# Import Libraries
###################################################################

import dash
import dash_core_components as dcc
import dash_html_components as html
import seaborn as sns
import pandas as pd
from ipywidgets import widgets
import numpy as np
from matplotlib.gridspec import GridSpec
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot
init_notebook_mode(connected=True)

import warnings
warnings.filterwarnings('ignore')

#alt.renderers.enable('notebook')
# Read data
###################################################################

df = pd.read_csv("Dataset_.csv")
region_app = pd.read_csv("Dataset_.csv")

#terror.columns
map_cols = ['year', 'countries', 'region', 'hf_score']
map_plot = pd.read_csv("Dataset_.csv", usecols = map_cols)
len(map_plot), len(map_plot.drop_duplicates())


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
trace1 = go.Bar(
    x=region_app['region'],
    y=region_app['pf_ss_women'],
    name='Women Security'
)
trace2 = go.Bar(
    x=region_app['region'],
    y=region_app['pf_ss'],
    name='Regional Security'
)

trace_1 = go.Bar(
    x=region_app['region'],
    y=region_app['pf_expression'],
    name='Expression of Speech'
)
trace_2 = go.Bar(
    x=region_app['region'],
    y=region_app['pf_expression_newspapers'],
    name='Expression of thoughts via Newspaper'
)
trace_3 = go.Bar(
    x=region_app['region'],
    y=region_app['pf_expression_internet'],
    name='Expression of thoughts via Internet'
)
trace_4 = go.Bar(
    x=region_app['region'],
    y=region_app['pf_expression_control'],
    name='Controlling the expressions'
)

#fig_bar = go.Figure(data=data, layout=layout)
#go.FigureWidget(data=data, layout=layout)
app.layout = html.Div(children=[
    html.H1(children='Global Freedom'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='graph1',
     figure={'data': 
    [dict(
    type='choropleth',
    locations=map_plot['countries'],
    locationmode='country names',
    z=round(map_plot['hf_score'],2),
    colorscale='Jet',
    reversescale=True,
    marker=dict(line=dict(color='rgb(180,180,180)'))
	)],
    'layout': (go.Layout(dict(
    title='Countries with Human Freedom Score',
    geo=dict(showframe=False, showcoastlines=False, projection=dict(type='mercator')),
    width=1000,
    height=1000,
   ))),
	
      }
    ),

	dcc.Graph(
        id='graph2',
        figure={
        'data':[trace1, trace2],
		'layout': (go.Layout(
		barmode='stack')),
	
      }
    ),
	
	dcc.Graph(
        id='graph3',
        figure={
        'data': [trace_1, trace_2, trace_3, trace_4],
		'layout': (go.Layout(barmode='group')),
	
      }
   ),
	
 ], )


if __name__ == '__main__':
    app.run_server(debug=True)