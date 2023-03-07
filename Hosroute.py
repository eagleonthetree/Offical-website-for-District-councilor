from navbar import Navbar
import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.graph_objects as go
import dash_core_components as dcc



nav = Navbar()

header = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(html.H1("醫院路綫指南",style={"margin": "15px 0px 20px 30px"}) )
            ]
        )
    ]
)

footer = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P(
                            "Copyright © 2021 Office of CHAN CHUN YUE"
                        )

                    ],
                    md=4, )]
        )
    ]
)

html1 = html.Iframe(src="https://www.google.com/maps/d/embed?mid=1IiU-88j5JO-_lRfFMBs853CP7FNy3KDl", width="600" ,height="600")




hosnav = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [html1
                    ]
                )

            ]
        ,justify="center")
    ]
)




def Hosroute():
    layout = html.Div([nav,
    header,
    hosnav,
    footer])
    return layout