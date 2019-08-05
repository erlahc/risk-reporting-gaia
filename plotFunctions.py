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
					'yaxis':dict(tickformat=',.1%',hoverformat=',.1%',tickangle=270),
					'legend':dict(orientation='h',xanchor='left',y=-0.40,font={'size':10}),
					'margin':dict(t=25,b=60,l=30,r=0)}
	}

def display_vintage_RAS(filtered_df,country):
	traces=[]
	titre='Vintage - '+ country
	columns=['Vintage6M','EW','CL']

	for i in columns:
		traces.append(go.Scatter(
				x=filtered_df['DATE'],
	            y=filtered_df[i],
	            name=i,
	            mode='lines+markers',
				))
		
	return{
		'data':traces,
		'layout': {	'xaxis':dict(categoryorder='array', categoryarray=filtered_df['DATE'].values, type="category"),
					'yaxis':dict(tickformat=',.1%',hoverformat=',.1%',tickangle=270),
					'legend':dict(orientation='h',xanchor='left',y=-0.40,font={'size':10}),
					'margin':dict(t=25,b=60,l=30,r=0)}
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
					'height':200,
					'margin':go.layout.Margin(l=30,r=0,b=60,t=25)}
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
					'xaxis':dict(categoryorder='array', categoryarray=filtered_df['DATE'].values, type="category"),
					'showlegend':False,
					'autosize':False,
					'height':200,
					'margin':go.layout.Margin(l=30,r=0,b=60,t=25)
					}
	}

def display_rr(filtered_df,metric,height=300):
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
					'height':height,
					'margin':dict(t=20,b=60,l=50,r=0)}
	}

def display_stock_data(filtered_df,metric):
	traces=[]
	traces.append(go.Bar(
		x=filtered_df['DATE'],
	    y=filtered_df[metric],
		))
		
	return{
		'data':traces,
		'layout': {
					'xaxis':dict(categoryorder='array', categoryarray=filtered_df['DATE'].values, type="category"),
					'showlegend':False,
					'autosize':False,
					'height':200,
					'margin':go.layout.Margin(l=30,r=0,b=60,t=25)
					}
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
	'layout':{
			'margin':go.layout.Margin(l=30,r=0,b=20,t=20)
		}
	}

def display_stock_data_donut_country(filtered_df,metric,date,country):
	values=[int(filtered_df[(filtered_df['COUNTRY']==country)&(filtered_df['DATE']==date)][metric]),
			int(filtered_df[(filtered_df['COUNTRY']!=country)&(filtered_df['DATE']==date)][metric].sum())]
	labels=[country,'Other']

	trace=go.Pie(labels=labels, values=values)

	return{
	'data':[trace],
	'layout':{
			'margin':go.layout.Margin(l=30,r=0,b=20,t=20)
		}
	}
