import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dash import Dash
from dash import html, dcc
from dashboard.components.header import Header
from dashboard.components.footer import Footer
from dashboard.components.sidebar import Sidebar

app = Dash(__name__, assets_folder='static')
app.title = 'Real-Time Financial Data Analysis'
def create_app():
    # app creation logic here
    pass
app.layout = html.Div([
    Header(),
    Sidebar(),
    html.Main([
        html.H1('Real-Time Financial Data Analysis Tool'),
        dcc.Graph(id='live-chart'),
    ]),
    Footer(),
])

if __name__ == '__main__':
    app.run_server(debug=True)
