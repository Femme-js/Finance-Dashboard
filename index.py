
import pandas as pd
import dash
import numpy as np
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go
from jupyter_dash import JupyterDash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


app = dash.Dash(__name__)


df = pd.read_csv("/home/femme_js/Downloads/transactions.csv")




df['Date'] = df['Date'].str[2:].str[:-5]



df['Amount'] = df['Amount'].map(lambda x: x.strip('-$').replace(",",""))

df = df.astype({"Amount": float}, errors='ignore')


df = df.astype({"Amount": float}, errors='ignore')



# NET WORTH OVER TIME





a = df['Amount']
a = list(map(float, a))

Net_Worth_Table = df.groupby('Date')['Amount'].sum().reset_index(name ='sum')
Net_Worth_Table['cumulative sum'] = Net_Worth_Table['sum'].cumsum()



Net_Worth_Table['Date'] = df['Date'].map(lambda x: x.strip('-/'))






# In[22]:



fig = px.line(Net_Worth_Table, x="Date", y="cumulative sum", title='Net Worth Over Time')


#Total Monthly Expense Chart



Total_Monthly_Expenses_Table = df.groupby('Date')['Amount'].sum().reset_index(name='sum')
Total_Monthly_Expenses_Table = Total_Monthly_Expenses_Table.rename(columns={'Date': 'Date', 'sum': 'TOTAL EXPENSE'})



Total_Monthly_Expenses_Table['Date'] = Total_Monthly_Expenses_Table['Date'].map(lambda x: x.strip('-/'))



fig = px.bar(Total_Monthly_Expenses_Table, x='Date', y='TOTAL EXPENSE')


#Expenses BreakDown Chart

Expenses_Breakdown_Chart = df.groupby('Category')['Amount'].sum().reset_index(name ='sum')


Expenses_Breakdown_Chart = px.line(Expenses_Breakdown_Chart, x='Category', y="sum", title="Expenses Breakdown", color = 'sum')





app.layout = html.Div([
    
    html.Div([
        html.H1(" Personal Finance Summary",style={'text-align':'center'}),
        dcc.Graph(figure = Net_Worth_Table)
    ]),
  
    html.Div([
        dcc.Graph(figure = Total_Monthly_Expenses_Table)
    ]),
    
    html.Div([
        dcc.Graph(figure = Expenses_Breakdown_Chart)

    ])
])
    

if __name__ == '__main__':
  app.run_server(debug = True)




