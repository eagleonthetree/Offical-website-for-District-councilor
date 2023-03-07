from navbar import Navbar
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash
import plotly.express as px
import dash_core_components as dcc
import pandas as pd
import json
import plotly.graph_objects as go

#ref:https://community.plotly.com/t/how-to-center-a-dbc-card-inside-of-a-dbc-row/50780

nav = Navbar()

footer = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P(
                            "Copyright © 2021 Office of CHAN CHUN YUE"
                            , style={"margin": "15px"})

                    ],
                    md=4, )]
        )
    ]
)


header = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(html.H1("黃大仙區數據(*under construction*)",style={"margin": "15px 0px 0px 0px"}) )
            ]
        ,justify="left")
    ]
)


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

card = dbc.Card(
    [dbc.CardHeader("標題"), dbc.CardBody(".")], className="h-100"
)


#graph
with open('map (4).geojson',encoding="utf-8") as f:
    data3 = json.load(f)
df = pd.read_excel("popu ver 1.xlsx")
fdf = df[df['Year']==2016]
fdf2 = fdf[fdf['No']=="2"]
fdf3= fdf2.filter(items=['Area',"Value"])


fig = px.choropleth_mapbox(fdf3, geojson=data3, locations='Area',
                           color_continuous_scale="bluered",
                           color="Value",
                           featureidkey="properties.Area",
                           mapbox_style="carto-positron",
                           zoom=12, center = {"lat": 22.342931, "lon": 114.197071},
                           opacity=0.6,
                           labels={'Value':'No of ppl'}
                          )

graph_card = dbc.Card(
    [dbc.CardHeader("WTS"), dbc.CardBody(dcc.Graph(figure=fig))],
    className="h-100",
)


card5 = dbc.Card(
    [dbc.CardHeader("指數"), dbc.CardBody("+23%")], className="h-100"
)


app.layout = dbc.Container(
    dbc.Row(
        [
            dbc.Col(
                [
                    dbc.Row([dbc.Col(card)] * 4, style={"height": "300px"}),
                    html.H2("黃大仙選區資料",style={"margin": "20px 0px 20px 0px"}),
                    dbc.Row(
                        [dbc.Col(graph_card)], style={"height": "400px"}
                    ),
                ],
                width=8,
            ),
            dbc.Col(card5, width=2),
        ],
        justify="center",
    ),
    fluid=True,
    className="mt-3",
)



def Wtsdata():
  layout = html.Div([nav,
                  header,
                  app.layout

                  ])
  return layout