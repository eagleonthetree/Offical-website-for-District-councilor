from navbar import Navbar
import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.graph_objects as go
import dash_core_components as dcc

nav = Navbar()



token = "pk.eyJ1IjoiZWFnbGVvbnRoZXRyZWUiLCJhIjoiY2txYnI3azR3MGQ4djJub2VweTV6aTJtYSJ9.GST597__HZ3U8nIkb5H5yQ"

fig = go.Figure(go.Scattermapbox(
    mode = "markers+text",
    lon = [113.936270,113.863249,113.995279,114.165652,114.158507,114.176235,114.168567,114.200571,114.190219,114.194044,114.221742,113.917754], lat = [22.316175,22.251924,22.258279,22.298904,22.286873,22.283150,22.293961,22.293286,22.301286,22.317907,22.306329,22.306726],
    marker = {'size': 12, 'symbol': [ "bus","bus","bus","ferry","ferry","ferry","ferry","ferry","ferry","ferry","ferry","airport"]},
    text = ["龍運巴士主要服務區域","新大嶼山巴士主要服務區域","新大嶼山巴士主要服務區域","中港客運碼頭","中環碼頭","灣仔碼頭","天星碼頭","北角碼頭","紅磡渡輪碼頭","九龍城渡輪碼頭","觀塘渡輪碼頭","香港機場"],textposition = "top right"))

#-245.8074187, 22.3426434
#-245.8280354, 22.2954497

coords = {"lat": 22.331181, "lon": 114.188266}
fig.update_layout(
    mapbox = {
        'accesstoken': token,
        'style': "outdoors", 'zoom': 10,
         'center':coords,},
    showlegend = False,title_text='香港交通網絡   **可放大縮小**')
fig.update_layout(height=600,width=1200,autosize=False)
fig.update_layout(font_size=20)

figmap = dbc.Container(
    [
        dbc.Row(
            [dbc.Col(
                dcc.Graph(figure=fig,config={
        'displayModeBar': False
    })
             ,width={"size": "auto","offset":"auto"})
            ]
        ,justify="center")
    ]
)



list_group = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
    dbc.ListGroup(
    [
        dbc.ListGroupItem(
            [dbc.Row([
                dbc.ListGroupItemHeading("巴士",style={"margin-left": "15px"}),
]),dbc.Row([
                dbc.Button("九巴路綫搜尋器",color="primary",href="https://search.kmb.hk/KMBWebSite/index.aspx?lang=tc",style={"margin": "1px 0px 0px 5px"},external_link=True,target="_blank"),
                dbc.Button("城/新巴路綫搜尋器",color="secondary",external_link=True,target="_blank",href="https://mobile.bravobus.com.hk/nwp3/?f=1&ds=&dsmode=1&l=0",style={"margin": "1px 0px 0px 5px"}),
                dbc.Button("龍巴路綫搜尋器", color="info",external_link=True,target="_blank",
                           href="http://www.lwb.hk/tc/"
                           ,style={"margin": "1px 0px 0px 5px"}),
                dbc.Button("新大嶼山巴士綫搜尋器", color="dark",external_link=True,target="_blank",
                           href="http://www.newlantaobus.com/route",
                           style={"margin": "1px 0px 0px 5px"}),
])]

        ),
        dbc.ListGroupItem(
            [
                dbc.ListGroupItemHeading("小巴"),
                dbc.Button("專線小巴路線",external_link=True,target="_blank", color="success", href="https://www.16seats.net/chi/index.html",style={"margin": "1px 0px 0px 5px"}),
                dbc.Button("紅色小巴路綫",external_link=True,target="_blank", color="primary",
                           href="http://www.i-busnet.com/minibus/",
                           style={"margin": "1px 0px 0px 5px"}),

            ]
        ),
dbc.ListGroupItem(
           [
             dbc.ListGroupItemHeading("地鐵"),
             dbc.Button("地鐵路綫搜尋器", color="info",external_link=True,target="_blank", href="http://www.mtr.com.hk/ch/customer/jp/"),

           ]

       ),
       dbc.ListGroupItem(
           [
             dbc.ListGroupItemHeading("的士"),
             dbc.Button("24小時電召的士服務詳程", color="primary",external_link=True,target="_blank", href="http://www.hk-tc.org/web/tc/content/9"),

           ]

       ),
        dbc.ListGroupItem(
           [
             dbc.ListGroupItemHeading("電車"),
             dbc.Button("互動路線圖", color="success",external_link=True,target="_blank", href="https://hktramways.com/tc/interactive-map/"),

           ]

       ),
dbc.ListGroupItem(
           [
             dbc.ListGroupItemHeading("渡輪"),
             dbc.Button("港內/港外渡輪服務", color="info",external_link=True,target="_blank", href="https://www.td.gov.hk/tc/transport_in_hong_kong/public_transport/ferries/service_details/index.html#i01"),

           ]

       )

    ]
)


                ,width={"size": 8,"offset": 2})
            ]
        )

    ]
)









header = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(html.H1("交通指南",style={"margin": "15px 0px 0px 30px"}) )
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


def Travel():
    layout = html.Div([nav,
    header,
    figmap,
    list_group,
    footer])
    return layout