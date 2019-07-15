# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from gaia import *
from plotFunctions import *
import ipdb

###
#APP INITIALIZATION
###
db=Gaia('granting_gen.csv','stock_gen.csv')
countries = db.df_stock['COUNTRY'].unique()
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
			dcc.Dropdown(id='id-countries',
					options=[{'label': i, 'value': i} for i in countries],
	                #value=countries[0]
	                value='PITA'
					)
			],className="col-md-2"),
		html.Div([
			html.H1(id='id-title',title='Stock summary',className="text-center")
		],className="col-md-10")
	],className="row"),
	#Row R0R1
	html.Div([
	#R0R1
		html.Div([
			dcc.Graph(id="id-R0R1")
			],className="col-md-4"),
	#Outstanding
		html.Div([
			dcc.Graph(id="id-os")
				],className="col-md-8")
		],className="row"),
	#Row R0R4
	html.Div([
	#R0R4
		html.Div([
			dcc.Graph(id="id-R0R4")
			],className="col-md-4"),
	#1ST Unpaid
		html.Div([
			dcc.Graph(id="id-1unpaid")
				],className="col-md-8")
		],className="row"),
	#Row R2+
	html.Div([
	#R2+
		html.Div([
			dcc.Graph(id="id-R2+")
			],className="col-md-4"),
	#% Encours
		html.Div([
			dcc.Graph(id="id-os-country-total")
			],className="col-md-4"),
	#%Encours
		html.Div([
			dcc.Graph(id="id-os-segment-country")
				],className="col-md-4")
		],className="row")
	],className="container-fluid")

###
#CALLBACK
###
@app.callback(
	[Output('id-R0R1', 'figure'),
	Output('id-R0R4', 'figure'),
	Output('id-R2+', 'figure'),
	Output('id-os', 'figure'),
	Output('id-1unpaid', 'figure'),
	Output('id-os-segment-country', 'figure'),
	Output('id-os-country-total', 'figure')],
    [Input('id-countries', 'value')])
def filter_rr_by_country(selected_country):
	return display_rr(db.get_rr(selected_country)[['COUNTRY','DATE','R0R1']],'R0R1'
		),display_rr(db.get_rr(selected_country)[['COUNTRY','DATE','R0R4']],'R0R4'
		),display_rr(db.get_rr(selected_country)[['COUNTRY','DATE','R2+']],'R2+'
		),display_stock_data(db.get_stock_data('OS',selected_country),'OS'
		),display_stock_data(db.get_stock_data('1UNPAID',selected_country),'1UNPAID'
		),display_stock_data_donut_segment(db.get_stock_data('OS',selected_country,'ALL'),'OS','201812'
		),display_stock_data_donut_country(db.get_stock_data('OS'),'OS','201812',selected_country)


if __name__ == '__main__':
	app.run_server(debug=True)