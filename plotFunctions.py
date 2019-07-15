import plotly.graph_objs as go

def display_vintage(filtered_df,country,segment=''):
	traces=[]
	if segment=='' or segment=='Other':
		titre='Vintage - '+ country
	else:
		titre='Vintage - '+ country + ' - ' + segment

	for i in filtered_df:
		traces.append(go.Scatter(
				x=filtered_df[i]['DATE'],
	            y=filtered_df[i][i],
	            name=i,
	            mode='lines+markers',
				))
		
	return{
		'data':traces,
		'layout': {	'xaxis':dict(categoryorder='array', categoryarray=filtered_df[i]['DATE'].values, type="category"),
					'yaxis':dict(tickformat=',.1%',hoverformat=',.1%'),
					'legend':dict(orientation='h',xanchor='left',y=-0.25),
					'margin':dict(t=20,b=20,l=50,r=0)}
	}

def display_multi_vintages(filtered_df,country,segment=''):
	traces=[]

	for i in filtered_df:
		traces.append(go.Scatter(
				x=filtered_df[i]['DATE'],
	            y=filtered_df[i][i],
	            name=i,
	            mode='lines+markers',
				))
		
	return{
		'data':traces,
		'layout': {'title':segment,
					'xaxis':dict(categoryorder='array', categoryarray=filtered_df[i]['DATE'].values, type="category"),
					'yaxis':dict(tickformat=',.0%',hoverformat=',.0%'),
					'showlegend':False,
					'autosize':False,
					'height':330,
					'margin':go.layout.Margin(l=25,r=10,b=60,t=50,pad=2)}
	}

def display_prod_fpd(filtered_df,country,prod_or_fpd,segment=''):
	traces=[]
	if segment=='' or segment=='Other':
		titre=prod_or_fpd+' - '+ country
	else:
		titre=prod_or_fpd+' - '+ country + ' - ' + segment

	traces.append(go.Bar(
		x=filtered_df['DATE'],
	    y=filtered_df[prod_or_fpd],
	    name=prod_or_fpd,
		))
		
	return{
		'data':traces,
		'layout': {'title':titre,
					'xaxis':dict(categoryorder='array', categoryarray=filtered_df['DATE'].values, type="category")}
	}

def display_rr(filtered_df,metric):
	traces=[]
	traces.append(go.Scatter(
			x=filtered_df['DATE'],
            y=filtered_df[metric],
            mode='lines+markers',
			))
		
	return{
		'data':traces,
		'layout': {	'xaxis':dict(categoryorder='array', categoryarray=filtered_df['DATE'].values, type="category"),
					'yaxis':dict(tickformat=',.1%',hoverformat=',.1%'),
					'showlegend':False,
					'margin':dict(t=20,b=100,l=50,r=0)}
	}

def display_stock_data(filtered_df,metric):
	traces=[]
	traces.append(go.Bar(
		x=filtered_df['DATE'],
	    y=filtered_df[metric],
		))
		
	return{
		'data':traces,
		'layout': {'title':metric,
					'xaxis':dict(categoryorder='array', categoryarray=filtered_df['DATE'].values, type="category")}
	}

def display_stock_data_donut_segment(filtered_df,metric,date):
	values=[]
	labels=[]
	for i in filtered_df['SEGMENT'].unique():
		values.append(int(filtered_df[(filtered_df['SEGMENT']==i)&(filtered_df['DATE']==date)][metric]))
		labels.append(i)
	trace=go.Pie(labels=labels, values=values)

	return{
	'data':[trace],
	'layout':{'title':metric + ' by segment'
		}
	}

def display_stock_data_donut_country(filtered_df,metric,date,country):
	values=[int(filtered_df[(filtered_df['COUNTRY']==country)&(filtered_df['DATE']==date)][metric]),
			int(filtered_df[(filtered_df['COUNTRY']!=country)&(filtered_df['DATE']==date)][metric].sum())]
	labels=[country,'Other']

	trace=go.Pie(labels=labels, values=values)

	return{
	'data':[trace],
	'layout':{'title':metric + ' by country'
		}
	}
