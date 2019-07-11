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
				dcc.Dropdown(id='id-countries',
						options=[{'label': i, 'value': i} for i in countries],
	                	value=countries[0]
					)
			],className="col-md-2"),
		html.Div([
			html.H1(id='id-title',title='Vintage summary',className="text-center")
		],className="col-md-10")
	],className="row"),
	#Row 1
	html.Div([
		html.Div([
			dcc.Graph(id="vintage-1")
			],className="col-md-3"),
		html.Div([
			dcc.Graph(id="vintage-2")
			],className="col-md-3"),
		html.Div([
			dcc.Graph(id="vintage-3")
			],className="col-md-3"),
		html.Div([
			dcc.Graph(id="vintage-4")
			],className="col-md-3")
		],className="row"),
	#Row 2
	html.Div([
		html.Div([
			dcc.Graph(id="vintage-5")
			],className="col-md-3"),
		html.Div([
			dcc.Graph(id="vintage-6")
			],className="col-md-3"),
		html.Div([
			dcc.Graph(id="vintage-7")
			],className="col-md-3"),
		html.Div([
			dcc.Graph(id="vintage-8")
			],className="col-md-3")
		],className="row")
	],className="container-fluid")

###
#CALLBACK
###
@app.callback(
	Output('id-title', 'children'),
    [Input('id-countries', 'value')])
def set_title(selected_country):
	a=selected_country + ' Vintage summary'
	return a

@app.callback(
	Output('vintage-1', 'figure'),
    [Input('id-countries', 'value')])
def set_multi_vintages(selected_country):
	try:
		a=db.df_granting[db.df_granting['COUNTRY']==selected_country]['SEGMENT'].unique()[0]
		return display_multi_vintages(db.get_vintage_by_segment(selected_country,a),selected_country,a)
	except IndexError:
		return 0
	
@app.callback(
	Output('vintage-2', 'figure'),
    [Input('id-countries', 'value')])
def set_multi_vintages(selected_country):
	try:
		a=db.df_granting[db.df_granting['COUNTRY']==selected_country]['SEGMENT'].unique()[1]
		return display_multi_vintages(db.get_vintage_by_segment(selected_country,a),selected_country,a)
	except IndexError:
		return 0

@app.callback(
	Output('vintage-3', 'figure'),
    [Input('id-countries', 'value')])
def set_multi_vintages(selected_country):
	try:
		a=db.df_granting[db.df_granting['COUNTRY']==selected_country]['SEGMENT'].unique()[2]
		return display_multi_vintages(db.get_vintage_by_segment(selected_country,a),selected_country,a)
	except IndexError:
		return 0

@app.callback(
	Output('vintage-4', 'figure'),
    [Input('id-countries', 'value')])
def set_multi_vintages(selected_country):
	try:
		a=db.df_granting[db.df_granting['COUNTRY']==selected_country]['SEGMENT'].unique()[3]
		return display_multi_vintages(db.get_vintage_by_segment(selected_country,a),selected_country,a)
	except IndexError:
		return 0

@app.callback(
	Output('vintage-5', 'figure'),
    [Input('id-countries', 'value')])
def set_multi_vintages(selected_country):
	try:
		a=db.df_granting[db.df_granting['COUNTRY']==selected_country]['SEGMENT'].unique()[4]
		return display_multi_vintages(db.get_vintage_by_segment(selected_country,a),selected_country,a)
	except IndexError:
		return 0

@app.callback(
	Output('vintage-6', 'figure'),
    [Input('id-countries', 'value')])
def set_multi_vintages(selected_country):
	try:
		a=db.df_granting[db.df_granting['COUNTRY']==selected_country]['SEGMENT'].unique()[5]
		return display_multi_vintages(db.get_vintage_by_segment(selected_country,a),selected_country,a)
	except IndexError:
		return 0

@app.callback(
	Output('vintage-7', 'figure'),
    [Input('id-countries', 'value')])
def set_multi_vintages(selected_country):
	try:
		a=db.df_granting[db.df_granting['COUNTRY']==selected_country]['SEGMENT'].unique()[6]
		return display_multi_vintages(db.get_vintage_by_segment(selected_country,a),selected_country,a)
	except IndexError:
		return 0

@app.callback(
	Output('vintage-8', 'figure'),
    [Input('id-countries', 'value')])
def set_multi_vintages(selected_country):
	try:
		a=db.df_granting[db.df_granting['COUNTRY']==selected_country]['SEGMENT'].unique()[7]
		return display_multi_vintages(db.get_vintage_by_segment(selected_country,a),selected_country,a)
	except IndexError:
		return 0

if __name__ == '__main__':
	app.run_server(debug=True)