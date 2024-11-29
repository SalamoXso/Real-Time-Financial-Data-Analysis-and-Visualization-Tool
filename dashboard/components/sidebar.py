from dash import html

def Sidebar():
    return html.Div([
        html.H3('Navigation'),
        html.Ul([
            html.Li(html.A('Home', href='/')),
            html.Li(html.A('About', href='/about')),
        ]),
    ], style={'width': '20%', 'float': 'left'})
