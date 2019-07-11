# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from gaia import *
from plotFunctions import *

###
#APP INITIALIZATION
###
db=Gaia('granting.csv','stock.csv')
countries = db.df_granting['COUNTRY'].unique()
app = dash.Dash()
app.css.append_css({
    "external_url": "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"
})

app.css.append_css({
    "external_url": 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

###
#LAYOUT
###
app.layout = html.Div([
	#Row title
	html.Div([
	#Column title
		html.Div([
			html.H1("Vintage summary",className="text-center")
		],className="col-md-12")
	],className="row"),
	#Row
	html.Div([
	#Column title
		html.Div([
			dcc.Dropdown(id='id-countries',
					options=[{'label': i, 'value': i} for i in countries],
                	value=countries[0]
				)
		],className="col-md-6"),
		html.Div([
			dcc.RadioItems(id='id-axes',
				labelStyle={'display': 'inline-block'}
				)
		],className="col-md-6"),
	],className="row"),
	#Row prod global by country
	html.Div([
	#Column vintage global by country
		html.Div([
			dcc.Graph(id="vintage-global")
			],className="col-md-6"),
	#Column prod + fpd global by country
		html.Div([
			dcc.Graph(id="vintage-segment")
				],className="col-md-6")
		],className="row"),
	#Prod ou FPD?
	html.Div([
		html.Div([
			dcc.RadioItems(id='id-prod-fpd',
					options=[{'label': i, 'value': i} for i in ['Production','FPD']],
                	value='Production',
                	labelStyle={'display': 'inline-block'}
				)
		],className="col-md-2"),
	],className="row"),
	#Row vintage + demand per segment
	html.Div([
	#Column vintage per segment
		html.Div([
			dcc.Graph(id="prod-fpd-global")
			],className="col-md-6"),
	#Column demand per segment
		html.Div([
			dcc.Graph(id="prod-fpd-segment")
			],className="col-md-6")
		],className="row")
	],className="container-fluid")

###
#CALLBACK
###

@app.callback(
	Output('id-axes', 'options'),
    [Input('id-countries', 'value')])
def set_axes_options(selected_country):
	a=list(db.df_granting[db.df_granting['COUNTRY']==selected_country]['SEGMENT'].unique())
	return [{'label':i,'value':i} for i in a]

@app.callback(
	Output('id-axes', 'value'),
    [Input('id-axes', 'options')])
def set_axes_value(available_options):
	return available_options[0]['value']

@app.callback(
	[Output('vintage-global', 'figure'),
	Output('prod-fpd-global', 'figure')],
    [Input('id-countries', 'value'),
    Input('id-prod-fpd', 'value')])
def filter_vintage_by_country(selected_country,selected_prod_fpd):
	return display_vintage(db.get_vintage_by_country(selected_country),selected_country
		),display_prod_fpd(db.get_production_by_country(selected_country),selected_country,selected_prod_fpd)

@app.callback(
    [Output('vintage-segment', 'figure'),
    Output('prod-fpd-segment', 'figure')],
    [Input('id-countries', 'value'),
     Input('id-axes', 'value'),
     Input('id-prod-fpd', 'value')])
def filter_vintage_by_segment(selected_country, selected_axes,selected_prod_fpd):
	return display_vintage(db.get_vintage_by_segment(selected_country, selected_axes),selected_country,selected_axes
		),display_prod_fpd(db.get_production_by_segment(selected_country, selected_axes),selected_country,selected_prod_fpd,selected_axes)

if __name__ == '__main__':
	app.run_server(debug=True)