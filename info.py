from navbar import Navbar
import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.figure_factory as ff
import dash_core_components as dcc



nav = Navbar()

table_header = [
    html.Thead(html.Tr([html.Th("聯絡方式"), html.Th(colSpan="2")]),style={"margin": "15px"})
]
row1 = html.Tr([html.Td("電話:"), html.Td(dbc.Button('55987648', color='primary',outline=True,href="tel:+852-55987648"),)])
row2 = html.Tr([html.Td("Telegram:"), html.Td("@DcYueWtsOffice"),html.Td("")])
row3 = html.Tr([html.Td("Facebook:"), html.Td(dbc.Button('YueWTS',target="_blank", color="info",outline=True,href="https://www.facebook.com/YueWTS/")),html.Td("")])
row4 = html.Tr([html.Td("辦事處地址:"), html.Td("黃大仙上邨啟善樓地下一號"),html.Td(dbc.Button('地圖',target="_blank", color="success",outline=True,href="https://goo.gl/maps/1HgpsxHjaaSvN39NA"))])
row5 = html.Tr([html.Td('辦公時間：星期一，二，四，五，六   10:00AM-1:00PM;2:00PM-6:00PM',"星期三   10:00AM-1:00PM"),html.Td("星期三   10:00AM-1:00PM"),html.Td("")])
row6 = html.Tr([html.Td('星期日及公衆假期'),html.Td('放假'),html.Td("")])

df = [
    dict(Task='星期一/ Monday', Start='2021-01-01 10:00:00', Finish='2021-01-01 13:00:00', Resource='辦公時間'),
    dict(Task='星期一/ Monday', Start='2021-01-01 13:00:00', Finish='2021-01-01 14:00:00', Resource='午飯時段'),
    dict(Task='星期一/ Monday', Start='2021-01-01 14:00:00', Finish='2021-01-01 18:00:00', Resource='辦公時間'),
    dict(Task='星期二/ Tuesday', Start='2021-01-01 10:00:00', Finish='2021-01-01 13:00:00', Resource='辦公時間'),
    dict(Task='星期二/ Tuesday', Start='2021-01-01 13:00:00', Finish='2021-01-01 14:00:00', Resource='午飯時段'),
    dict(Task='星期二/ Tuesday', Start='2021-01-01 14:00:00', Finish='2021-01-01 18:00:00', Resource='辦公時間'),
    dict(Task='星期三/ Wednesday', Start='2021-01-01 10:00:00', Finish='2021-01-01 13:00:00', Resource='辦公時間'),
    dict(Task='星期三/ Wednesday', Start='2021-01-01 13:00:00', Finish='2021-01-01 14:00:00', Resource='午飯時段'),
    dict(Task='星期四/ Thursday', Start='2021-01-01 10:00:00', Finish='2021-01-01 13:00:00', Resource='辦公時間'),
    dict(Task='星期四/ Thursday', Start='2021-01-01 13:00:00', Finish='2021-01-01 14:00:00', Resource='午飯時段'),
    dict(Task='星期四/ Thursday', Start='2021-01-01 14:00:00', Finish='2021-01-01 18:00:00', Resource='辦公時間'),
    dict(Task='星期五/ Friday', Start='2021-01-01 10:00:00', Finish='2021-01-01 13:00:00', Resource='辦公時間'),
    dict(Task='星期五/ Friday', Start='2021-01-01 13:00:00', Finish='2021-01-01 14:00:00', Resource='午飯時段'),
    dict(Task='星期五/ Friday', Start='2021-01-01 14:00:00', Finish='2021-01-01 18:00:00', Resource='辦公時間'),
    dict(Task='星期六/ Saturday', Start='2021-01-01 10:00:00', Finish='2021-01-01 13:00:00', Resource='辦公時間'),
    dict(Task='星期六/ Saturday', Start='2021-01-01 13:00:00', Finish='2021-01-01 14:00:00', Resource='午飯時段'),
    dict(Task='星期六/ Saturday', Start='2021-01-01 14:00:00', Finish='2021-01-01 18:00:00', Resource='辦公時間'),

]


colors = dict(辦公時間='rgb(51, 204, 204)',午飯時段='rgb(0, 240, 0)')

fig = ff.create_gantt(df, colors=colors, index_col='Resource', title='辦事處開放時間(星期日及公衆假期放假) ***辦事處由2021年7月12號起會暫停對外開放，敬請原諒***',
                      show_colorbar=True, bar_width=0.4, showgrid_x=True, group_tasks=True)

fig.update_layout(xaxis_title="每日辦公時段",font=dict(family="Balto",size=18))
fig.layout.xaxis.rangeselector = None
fig.update_layout(title_font_size=23)

table_body = [html.Tbody([row1, row2, row3, row4,row5,row6])]
table = dbc.Table(table_header + table_body, bordered=True)
timetable = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [dcc.Graph(figure=fig,config={
        'displayModeBar': False
    })

                    ]
                )
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

infosection = dbc.Container(
    [dbc.Row([
            dbc.Col(html.H1("聯絡我們"), className="mb-2",style={"margin":"15px 0px 0px 0px"})
        ]),
        dbc.Row(
            [
                dbc.Col(
                    [table

                    ],style={"margin":"15px 0px 0px 0px"}
                )
            ]
        )
    ]
)




def Info():
   layout = html.Div([
       nav,
       timetable,
       infosection,
       footer
    ])
   return layout

