import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import App, build_graph
from homepage import Homepage
from info import Info
from welfare import Welfare
from travel import Travel
from wtsdata import Wtsdata
from Hosroute import Hosroute
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.JOURNAL])

app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id = 'url', refresh = False),
    html.Div(id = 'page-content')
])


@app.callback(Output('page-content', 'children'),
            [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/time-series':
        return App()
    elif pathname =='/info':
        return Info()
    elif pathname == '/welfare':
        return Welfare()
    elif pathname == '/travel':
        return Travel()
    elif pathname == '/wtsdata':
        return Wtsdata()
    elif pathname == '/Housroute':
        return Hosroute()
    else:
        return Homepage()

@app.callback(
    Output('output', 'children'),
    [Input('pop_dropdown', 'value')]
)
def update_graph(city):
    graph = build_graph(city)
    return graph

@app.callback(
    Output("barcol2", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("barcol2", "is_open")],
)


def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


if __name__ == '__main__':
    app.run_server(debug=True)



