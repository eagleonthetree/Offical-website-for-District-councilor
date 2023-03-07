import dash_bootstrap_components as dbc
import dash_html_components as html


#html.A(html.Button('Submit feedback!', className='three columns'),
#    href='https://github.com/czbiohub/singlecell-dash/issues/new')
#)

menu = dbc.DropdownMenu(
                nav=True,
                in_navbar=True,
                label="查詢",
                children=[
                    dbc.DropdownMenuItem("福利及常用電話",href='/welfare'),
                    dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem("交通",href="/travel"),
                    dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem("黃大仙區數據",href='/wtsdata'),
                    dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem("醫院路綫指南",href='/Housroute')
                ],
            )

def Navbar():
    navbar = dbc.Navbar(
      [
          html.A(
              dbc.Row(
                [
                      dbc.Col(html.Img(src="/assets/logo2.PNG", height="40px"))

                  ],justify="left",
                  align="left",
                  no_gutters=True,
              ),
              href="/home",
          ),
          dbc.Col(html.A(html.Button('武肺資訊', className='ml-auto'),
                         href='https://wars.vote4.hk/updates',target="_blank"),style={"margin-right":"1px"} ,width={"size": "auto"}),
        dbc.Col([
          dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
          dbc.Collapse(
              dbc.Nav(
              [menu],className="ml-auto",  navbar=True),
              id="barcol2",
              navbar=True,style={"margin-right":"40px"}
          ),
        ])

      ],
    color="#0f5647",
    dark=True,
)

    return navbar


def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open