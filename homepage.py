import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from navbar import Navbar
nav = Navbar()

simple_jumbotron = dbc.Jumbotron(
    [
        html.H1("歡迎", className="display-3"),
        html.H3("*多謝各位街坊支持，阿裕已經於七月八日辭去黃大仙區議員一職*",style={'color': 'green'}),
        html.P(
            "陳俊裕區議員辦事處 任期:(2020年1月1日至2021年7月11日)",
            className="lead",
        ),
        html.Hr(className="my-2"),
        html.P(
            "辦公時間：星期一，二，四，五，六   10:00AM - 1:00PM ; 2:00PM - 6:00PM / 星期三   10:00AM - 1:00PM"
        ),

        html.P(dbc.Button("聯絡我們", color="primary",external_link=True,href='/info'), className="lead"),
    ]
)


simple_card = dbc.Card(
    [
        dbc.CardImg(src="/assets/meweheader.JPG", top=True),
        dbc.CardBody(
            [
                html.H4("Mewe", className="card-title"),

                dbc.Button("follow us",external_link=True,target="_blank", color="primary",href="https://mewe.com/p/%E9%99%B3%E4%BF%8A%E8%A3%95-%E9%98%BF%E8%A3%95"),
            ]
        ),
    ],
    style={"width": "20rem"},
)

simple_card2 = dbc.Card(
    [
        dbc.CardImg(src="/assets/signal.png", top=True),
        dbc.CardBody(
            [
                html.H4("Signal", className="card-title"),

                dbc.Button("follow us",external_link=True,target="_blank", color="primary",href="tel:+852-60138164"),
            ]
        ),
    ],
    style={"width": "20rem"},
)



body = dbc.Container(
    [dbc.Row([
        dbc.Col([
            simple_jumbotron
        ])

    ]),

       ],
className="mt-4"
)

facebook = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(html.Iframe(src="https://www.facebook.com/plugins/page.php?href=https%3A%2F%2Fwww.facebook.com%2FYueWTS%2F%3Ffref%3Dmentions%26__tn__%3DK-R&tabs=timeline&width=350&height=500&small_header=true&adapt_container_width=true&hide_cover=false&show_facepile=true&appId", width="350", height="500")
                ,width={"size": "auto","offest":3,"order":1},),
                dbc.Col(
                    [
                     simple_card,simple_card2
                    ],width={"size":"auto","offest":"auto","order":2})
            ],justify="center",style={"margin-top":"30px"}
        )
    ]
)



footer = html.Div([
    dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P(
                            "Copyright © 2021 Office of CHAN CHUN YUE"
                        ,style={"margin": "15px"}),
                        html.Label(["This application is created by ", html.A('eagleonthetree :)', href="https://github.com/eagleonthetree")],style={"font-size":"10px"})


                    ]
                    )]
        )
    ]
)]
)

layout_group_cards = dbc.CardGroup(
    [
        dbc.Card(
            dbc.CardBody(
                [
                    html.H5("交通", className="card-title"),
                    html.P(
                        "各類交通的路綫搜尋器"
                        ,
                        className="card-text",style={"margin-bottom":"40px"}
                    ),
                    dbc.Button(
                        "前往頁面", color="success", className="mt-auto",href="/travel"),
                ]
            )
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.H5(["福利及常用電話",dbc.Badge("熱門",color="primary" ,className="ml-1")]),
                    html.P(
                        "各項公共福利的申請資格，申請方法和所需的表格下載，以及常用電話列表",
                        className="card-text",
                    ),
                    dbc.Button(
                        "前往頁面", color="warning", className="mt-auto",href="/welfare"
                    ),
                ]
            )
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.H5("黃大仙區數據儀表板", className="card-title"),
                    html.P(
                        "此頁面提供了黃大仙區的各種數據，以供居民參考"
                        ,
                        className="card-text",
                    ),
                    dbc.Button(
                        "前往頁面", color="info", className="mt-auto",href="/wtsdata"
                    ),
                ]
            )
        ),
    ]
)



layout_group_cards2 = dbc.CardGroup(
    [
        dbc.Card(
            dbc.CardBody(
                [
                    html.H5("醫院路綫指南", className="card-title"),
                    html.P(
                        "Google map路綫指南",
                        className="card-text"
                    ),
                    dbc.Button(
                        "前往頁面", color="danger", className="mt-auto",href="/Housroute"),
                ]
            )
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.H5("公屋租金減免計算機", className="card-title"),
                    html.P(
                        "由楊彧議員辦事處製作",
                        className="card-text",
                    ),
                    dbc.Button(
                        "前往計算機", color="secondary", className="mt-auto",href="https://script.google.com/macros/s/AKfycbyqlWhgGR5BIW8VVxKCO8Vy-OKVgaOd5e1UgyEG05elYZilf3U/exec"
                    ),
                ]
            )
        )
    ]
)




cardbox = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                       layout_group_cards
                    ]
                ,width={"size":12})
            ]
        ,justify="center"),
        dbc.Row(
            [
                dbc.Col(
                    [
                      layout_group_cards2
                    ],width={"size":10}
                )
            ]
        ,justify="center")
    ]
)




def Homepage():
    layout = html.Div([
    nav,
    body,
    cardbox,
    facebook,
    footer
    ])
    return layout

app = dash.Dash(__name__, external_stylesheets = [dbc.themes.UNITED])
app.layout = Homepage()
if __name__ == "__main__":
    app.run_server()


