# coding: utf-8

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import os
from gaia import *
from plotFunctions import *

app = dash.Dash(__name__)
server = app.server
app.config['suppress_callback_exceptions']=True

db=Gaia('granting_gen.csv','stock_gen.csv')
countries = db.df_stock['COUNTRY'].unique()

def print_button():
    printButton = html.A(['Print PDF'],className="button no-print print",style={'position': "absolute", 'top': '-40', 'right': '0'})
    return printButton

# includes page/full view
def get_logo():
    logo = html.Div([

        html.Div([
            html.Img(src='http://logonoid.com/images/vanguard-logo.png', height='40', width='160')
        ], className="ten columns padded"),

        html.Div([
            dcc.Link('Full View   ', href='/full-view')
        ], className="two columns page-view no-print")

    ], className="row gs-header")
    return logo


def get_header():
    header = html.Div([

        html.Div([
            html.H5(
                'Vanguard 500 Index Fund Investor Shares')
        ], className="twelve columns padded")

    ], className="row gs-header gs-text-header")
    return header


def get_menu():
    menu = html.Div([

        dcc.Link('Overview   ', href='/overview', className="tab first"),

        dcc.Link('Granting   ', href='/granting', className="tab"),

        dcc.Link('Vintages   ', href='/vintages', className="tab"),

        dcc.Link('Stock   ', href='/stock', className="tab"),

    ], className="row ")
    return menu

def get_country(countryList):
  countries=html.Div([
              dcc.Dropdown(id='id-countries',
              options=[{'label': i, 'value': i} for i in countryList],
              value=countryList[0]
              )
            ],className="row ")
  return countries

def get_graph1(name,height=300,width=340,bs_type='six columns',title='',jump=''):
  fig=dcc.Graph(id=name,
        figure={'layout':go.Layout(
        autosize = False,
        showlegend = False,
        height = height,
        width = width,
        margin={'l':20,'r':20,'t':20,'b':20},
        xaxis=dict(rangemode='tozero',autorange=True),
        yaxis=dict(rangemode='tozero',autorange=True)
        )
      }
    )
  if jump!='':
    return html.Div([html.H6(jump,
                            className="gs-header gs-text-header padded"),fig],className=bs_type)
  else:
    return html.Div([fig],className=bs_type)

def get_graph_with_dropdown(name,height=300,dropdown=['PITA','PPOR']):
  graph=html.Div([
    dcc.Dropdown(id='id-countries',
          options=[{'label': i, 'value': i} for i in dropdown],
          value=dropdown[0]
    ),
    dcc.Graph(id=name,
      figure={'layout':go.Layout(
        autosize = False,
        showlegend = False,
        height = height,
        width = 340,
        margin={'l':20,'r':20,'t':20,'b':20},
        xaxis=dict(rangemode='tozero',autorange=True),
        yaxis=dict(rangemode='tozero',autorange=True)
        )
      }
    )], 
    className="six columns")
  return graph

## Page layouts
overview = html.Div([  # page 1
        print_button(),
        html.Div([
            get_menu(),
            get_country(countries),
            # Row 3
                html.Div([
                  html.Div([
                    html.H6('Vintage',
                            className="gs-header gs-text-header padded")], className="six columns"),
                  html.Div([
                    html.H6('R0R1',
                            className="gs-header gs-table-header padded")], className="six columns")
                ], className="row "),
                html.Div([
                  get_graph1('RAS-vintage-6M'),
                  get_graph1('RAS-R0R1')
            ], className="row "),
                html.Div([
                  html.Div([
                    html.H6('R0R4',
                            className="gs-header gs-text-header padded")], className="six columns"),
                  html.Div([
                    html.H6('R2+',
                            className="gs-header gs-table-header padded")], className="six columns")
                ], className="row "),
                html.Div([
                  get_graph1('RAS-R0R4'),
                  get_graph1('RAS-R2+')
            ], className="row ")
            ], className="subpage")
    ], className="page")

#Page 2
granting = html.Div([  # page 3
              print_button(),
              html.Div([
                get_menu(),
                get_country(countries),
              # Row ``
                html.Div([
                  get_graph1(name='vintage-global',height=250,jump='All segments'),
                  get_graph_with_dropdown(name='vintage-segment',height=250,dropdown=['Auto','Retail']),
                ], className="row "),
                html.Div([
                  dcc.RadioItems(id='id-prod-or-fpd',
                                  options=[{'label': i, 'value': i} for i in ['Production','FPD']],
                                  value='Production',
                                  labelStyle={'display': 'inline-block'}
                  )
                ], className="row "),
                html.Div([
                  get_graph1('prod-fpd-global',250),
                  get_graph1('prod-fpd-segment',250)
                ], className="row "),
                html.Div([
                  get_graph1('id-prod-country',250),
                  get_graph1('id-prod-segment',250)
                ], className="row "),
              ], className="subpage")
          ], className="page")

vintages = html.Div([  # page 3
        print_button(),
        html.Div([
            get_menu(),
            get_country(countries),
            # Row ``
            html.H6(["Vintage analysis"],
                            className="gs-header gs-table-header padded"),
            html.Div([
              get_graph1('vintage1',175),
              get_graph1('vintage2',175),
            ], className="row "),
            html.Div([
                  get_graph1('vintage3',175),
                  get_graph1('vintage4',175),
            ], className="row "),
            html.Div([
                  get_graph1('vintage5',175),
                  get_graph1('vintage6',175),
            ], className="row "),
            html.Div([
                  get_graph1('vintage7',175),
                  get_graph1('vintage8',175),
            ], className="row "),
            # Row 2
        ], className="subpage")
    ], className="page")

stock = html.Div([  # page 3
              print_button(),
              html.Div([
                get_menu(),
                get_country(countries),
              # Row ``
                html.H6(["Stock analysis"],
                            className="gs-header gs-table-header padded"),
                html.Div([
                  get_graph1('id-R0R1',250,230,'four columns'),
                  get_graph1('id-R0R4',250,230,'four columns'),
                  get_graph1('id-R2+',250,230,'four columns'),
                ], className="row "),
                html.Div([
                  get_graph1('id-os-global',250),
                  get_graph1('id-os-segment',250)
                ], className="row "),
                html.Div([
                  get_graph1('id-os-country-over-all',250),
                  get_graph1('id-os-segment-over-country',250)
                ], className="row "),
              ], className="subpage")
          ], className="page")

noPage = html.Div([  # 404

    html.P(["404 Page not found"])

    ], className="no-page")

# Describe the layout, or the UI, of the app
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# Update page
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/' or pathname == '/overview':
        return overview
    elif pathname == '/granting':
        return granting
    elif pathname == '/vintages':
        return vintages
    elif pathname == '/stock':
        return stock
    elif pathname == '/rollrates':
        return rollrates
    elif pathname == '/full-view':
        return overview,granting,vintages,stock,rollrates
    else:
        return noPage

@app.callback(
  [Output('RAS-vintage-6M', 'figure'),
  Output('RAS-R0R1', 'figure'),
  Output('RAS-R0R4', 'figure'),
  Output('RAS-R2+', 'figure')],
  [Input('id-countries', 'value')])
def update_ras_charts(selected_country):
  return display_vintage(db.get_vintage(selected_country),selected_country
    ),display_rr(db.get_rr(selected_country)[['COUNTRY','DATE','R0R1']],'R0R1'
    ),display_rr(db.get_rr(selected_country)[['COUNTRY','DATE','R0R4']],'R0R4'
    ),display_rr(db.get_rr(selected_country)[['COUNTRY','DATE','R2+']],'R2+'
    )


external_css = ["https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",
                "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
                "//fonts.googleapis.com/css?family=Raleway:400,300,600",
                "https://codepen.io/bcd/pen/KQrXdb.css",
                "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"]

for css in external_css:
    app.css.append_css({"external_url": css})

if __name__ == '__main__':
    app.run_server(debug=True)