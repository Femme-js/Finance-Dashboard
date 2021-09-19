import os

import dash
import dash_core_components as dcc
import dash_html_components as html



app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div([
    
])

@app.callback(

)



if __name__ == '__main__':
    app.run_server(debug=True)
