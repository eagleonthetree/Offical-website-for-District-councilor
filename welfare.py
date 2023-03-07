from navbar import Navbar
import dash_bootstrap_components as dbc
import dash_html_components as html

nav = Navbar()

card_content_1 = [
    dbc.CardImg(src="assets/unnamed.jpg", top=True),
    dbc.CardBody(
        [
            html.H5("普通長者生活津貼", className="card-title"),
            html.P(
                "普通長者生活津貼及高額長者生活津貼旨在為本港65歲或以上有經濟需要的長者每月提供特別津貼，以補助他們的生活開支。普通長者生活津貼為2,845元",
                className="card-text",
            ),
            dbc.Button("瞭解申請資格",target="_blank", color="primary",href="https://www.swd.gov.hk/oala/#s4",style={"margin-right": "1px"}),
            dbc.Button("下載表格",target="_blank", color="success",href="https://www.swd.gov.hk/tc/index/site_pubsvc/page_socsecu/sub_ssallowance/")
        ]
    ),
]

card_content_2 = [
    dbc.CardImg(src="assets/unnamed.jpg", top=True),
    dbc.CardBody(
        [
            html.H5("高額長者生活津貼", className="card-title"),
            html.P(
                "高額長者生活津貼旨在為本港65歲或以上有經濟需要的長者每月提供特別津貼，以補助他們的生活開支。高額長者生活津貼現時每月金額為3,815元。",
                className="card-text",
            ),
            dbc.Button("瞭解申請資格",target="_blank", color="primary",href="https://www.swd.gov.hk/oala/#s4",style={"margin-right": "1px"}),
            dbc.Button("下載表格",target="_blank", color="success",href="https://www.swd.gov.hk/tc/index/site_pubsvc/page_socsecu/sub_ssallowance/")
        ]
    ),
]

card_content_3 = [
    dbc.CardImg(src="/assets/roujin_family.png", top=True),
    dbc.CardBody(
        [
            html.H5("綜援", className="card-title"),
            html.P(
                "綜援計劃的目的﹐是以入息補助方法﹐為那些在經濟上無法自給的人士提供安全網﹐使他們的入息達到一定水平﹐以應付生活上的基本需要。",
                className="card-text",
            ),
            dbc.Button("瞭解申請資格及津貼金額",target="_blank", color="primary",href="https://www.1823.gov.hk/tc/faq/what-are-the-eligibility-criteria-of-comprehensive-social-security-assistance-cssa-what-is-the-amount-of-assistance-payable",style={"margin-right": "1px"}),
            dbc.Button("申請方法",target="_blank", color="success",href="https://www.1823.gov.hk/tc/faq/what-are-the-application-procedures-and-the-payment-arrangement-for-comprehensive-social-security-assistance-scheme") ]
    ),
]

card_content_4 = [
    dbc.CardImg(src="/assets/roujin_egao.png", top=True),
    dbc.CardBody(
        [
            html.H5("高齡津貼", className="card-title"),
            html.P(
                "高齡津貼是社會福利署為70歲或以上的香港居民，每月提供的現金津貼，以應付因年老而引致的特別需要。申請人不需通過入息審查。由2021年2月1日起，高齡津貼的每月金額為$1,475。",
                className="card-text",
            ),
            dbc.Button("申請資格",target="_blank", color="primary",href="https://www.1823.gov.hk/tc/faq/what-are-the-eligibility-criteria-of-old-age-allowance-what-is-the-amount-of-assistance-payable",style={"margin-right": "1px"}),
            dbc.Button("下載表格",target="_blank", color="success",href="https://www.swd.gov.hk/tc/index/site_pubsvc/page_socsecu/sub_ssallowance/")
        ]
    ),
]

card_content_5 = [
    dbc.CardImg(src="/assets/eprice_1_31c57d9240969b818864fefe4b564a71.png", top=True),
    dbc.CardBody(
        [
            html.H5("電子消費卷", className="card-title"),
            html.H5(["5,000元電子消費券", dbc.Badge("New", color="danger",className="ml-1")]),
            dbc.Button("立即登記",target="_blank", color="primary",href="https://www.consumptionvoucher.gov.hk/tc/register.html"),
        ]
    ),
]

card_content_6 = [
    dbc.CardImg(src="/assets/N5262_CLP_PC_2020_Web_1440x500_C_v3_20200407.jpg", top=True),
    dbc.CardBody(
        [
            html.H5(["中電全心傳電", dbc.Badge("熱門",color="primary" ,className="ml-1")]),
            html.H6(["合資格受惠人士:每戶500港元的電費資助"]),
            html.H6(["劏房住戶:每戶600港元電費資助"]),
            html.P("如果你屬於65歲或以上獨居／雙老長者、低收入人士、殘疾人士： 請親身前往協辦的非政府機構遞交申請",
            className="card-text",
            ),
            html.H6(["機構名單(各區)："]),
            dbc.Button("九龍區",target="_blank", color="primary",href="https://www.clp.com.hk/zh/my-home-site/Documents/%E5%85%A8%E5%BF%83%E5%82%B3%E9%9B%BB%E9%A1%9E%E5%88%A51-%E9%A1%9E%E5%88%A53%E5%8D%94%E8%BE%A6%E9%9D%9E%E6%94%BF%E5%BA%9C%E6%A9%9F%E6%A7%8B%E5%90%8D%E5%96%AE(%E4%B9%9D%E9%BE%8D%E5%8D%80).pdf?_ga=2.255008840.1163005534.1624524932-1976131641.1624524932"),
            dbc.Button("新界區",target="_blank", color="info",href="https://www.clp.com.hk/zh/my-home-site/Documents/%E5%85%A8%E5%BF%83%E5%82%B3%E9%9B%BB%E9%A1%9E%E5%88%A51-%E9%A1%9E%E5%88%A53%E5%8D%94%E8%BE%A6%E9%9D%9E%E6%94%BF%E5%BA%9C%E6%A9%9F%E6%A7%8B%E5%90%8D%E5%96%AE(%E6%96%B0%E7%95%8C%E5%8D%80).pdf?_ga=2.220292824.1163005534.1624524932-1976131641.1624524932",style={"margin-left": "1px"}),
            dbc.Button("離島或香港區",target="_blank", color="secondary",href="https://www.clp.com.hk/zh/my-home-site/Documents/%E5%85%A8%E5%BF%83%E5%82%B3%E9%9B%BB%E9%A1%9E%E5%88%A51-%E9%A1%9E%E5%88%A53%E5%8D%94%E8%BE%A6%E9%9D%9E%E6%94%BF%E5%BA%9C%E6%A9%9F%E6%A7%8B%E5%90%8D%E5%96%AE(%E9%A6%99%E6%B8%AF%E5%8F%8A%E9%9B%A2%E5%B3%B6%E5%8D%80).pdf?_ga=2.220292824.1163005534.1624524932-1976131641.1624524932",style={"margin-left": "1px"}),
            html.P("劏房住戶協辦機構名單：",className="card-text",style={"margin-top":"10px"}),
            dbc.Button("劏房住戶",target="_blank", color="primary",href="https://www.clp.com.hk/zh/my-home-site/Documents/%E5%85%A8%E5%BF%83%E5%82%B3%E9%9B%BB%E9%A1%9E%E5%88%A54-%E5%8A%8F%E6%88%BF%E4%BD%8F%E6%88%B6%E5%8D%94%E8%BE%A6%E9%9D%9E%E6%94%BF%E5%BA%9C%E6%A9%9F%E6%A7%8B%E5%90%8D%E5%96%AE.pdf?_ga=2.220292824.1163005534.1624524932-1976131641.1624524932")

        ]
    ),
]

card_content_7 = [
    dbc.CardImg(src="/assets/food.JPG", top=True),
    dbc.CardBody(
        [
            html.H5("短期食物援助服務", className="card-title"),
            html.P(
                "為難以應付日常食物開支的個人或家庭所提供的短期食物援助",
                className="card-text",
            ),
            dbc.Button("申請資格",target="_blank",color="primary",href="https://www.swd.gov.hk/storage/asset/section/2493/tc/Income_and_Asset_Limits_for_STFASPs_(June_2021).pdf",style={"margin-right":"1px"}),
            dbc.Button("黃大仙申請機構地址",target="_blank", color="success",href="http://www.abmsbc.org.hk/ABMS_contact_us/"),
        ]
    ),
]

card_content_8 = [
    dbc.CardImg(src="/assets/rent.JPG", top=True),
    dbc.CardBody(
        [
            html.H5("公屋租金減免", className="card-title"),
            html.P(
                "透過寬減公屋租金而援助暫時有經濟困難的人士",
                className="card-text",
            ),
            dbc.Button("申請資格",target="_blank", color="primary",href="https://www.housingauthority.gov.hk/tc/public-housing/rent-related-matters/rent-assistance-scheme/index.html"),
            html.H6(["請向你的屋邨辦事處索取申請表格"],style={"margin-top":"5px"}),
        ]
    ),
]


card_content_9 = [
    dbc.CardImg(src="/assets/fm.JPG", top=True),
    dbc.CardBody(
        [
            html.H5("在職家庭津貼", className="card-title"),
            html.P(
                "",
                className="card-text",
            ),
            dbc.Button("申請方法",target="_blank", color="primary",href="https://www.wfsfaa.gov.hk/wfao/tc/how_to_apply.htm",style={"margin-right": "1px"}),
            dbc.Button("申請資格",target="_blank", color="secondary",href="https://www.wfsfaa.gov.hk/wfao/tc/eligibility.htm",style={"margin-right": "1px"}),
            dbc.Button("下載表格",target="_blank", color="success",href="https://www.wfsfaa.gov.hk/wfao/tc/downloadable.htm")
        ]
    ),
]


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


layout_columns_cards = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
        dbc.CardColumns(
    [
        dbc.Card(card_content_1, color="light"),
        dbc.Card(card_content_2, color="light"),
        dbc.Card(card_content_3, color="light"),
        dbc.Card(card_content_5, color="light"),
        dbc.Card(card_content_6, color="light"),
        dbc.Card(card_content_4, color="light"),
        dbc.Card(card_content_7, color="light"),
        dbc.Card(card_content_8, color="light"),
        dbc.Card(card_content_9, color="light"),

    ],style={"margin": "15px 0px 0px 0px"})


                )
            ]
        )

    ]
)






simple_card3 = dbc.Card(
    [
        dbc.CardImg(src="/assets/info.png", top=True),
        dbc.CardBody(
            [
                html.H4("常用電話", className="card-title"),

html.P("District Tenancy Management Office/Estate Office"),
html.P("黃大仙上邨"),
html.P("Upper Wong Tai Sin Estate"),
html.P("黃大仙區租約事務管理處（四）"),
html.P("wong Tai Sin District Tenancy Management Office (4) , 電話/TEL：3572 0040"),
html.Br(),
html.P("屋邨物業管理 ："),
html.P("Property Management"),
html.P("創毅物業服務顧問有限公司"),
html.P("Creative Property Services Consultants Ltd. , 電話/TEL：2321 2004"),
html.Br(),
html.P("黃大仙下(二)邨"),
html.P("Lower Wong Tai Sin (2) Estate"),
html.P("黃大仙下二邨分區租約事務管理辦事處"),
html.P("Wong Tai Sin District Tenancy Management Office, 電話/TEL：2326 8962"),
html.Br(),
html.P("屋邨物業管理："),
html.P("Property Management"),
html.P("宜居顧問服務有限公司"),
html.P("Easy Living Consultant Limited, 電話/TEL：2726 5675"),
html.Br(),
html.P("水務署"),
html.P("Water Supplies Department"),
html.P("爆水管"),
html.P("pipe burst,電話/TEL：2854 5000"),
html.P("按/PRESS 1 > 0 > 0"),
html.Br(),
html.P("供水故障" ),
html.P("water outage,電話/TEL：2854 5000"),
html.P("按/ PRESS1 > 0 > 1"),
html.Br(),
html.P("煤氣24小時客戶服務熱線"),
html.P("Towngas 24-Hour Customer Service Hotline,電話/TEL：2880 6988"),
html.Br(),
html.P("中電緊急服務熱線,電話/TEL：2728 8333"),
html.Br(),
html.P("民政署法律諮詢 - 法律意見及指導"),
html.P("Free Legal Advice Scheme,電話/TEL：2322 9701（上午9:00至下午7:00）"),
html.Br(),
html.P("慈雲山社會保障辦事處"),
html.P("Tsz Wan Shan Social Security Field Unit,電話/TEL: 2327 5083"),
html.Br(),
html.P("黃大仙綜合家庭服務中心"),
html.P("Wong Tai Sin Integrated Family Service Centre,電話/TEL: 2327 4973"),
                  ]
                )
            ],style={"width": "auto"},
        )

INFOCARD = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        simple_card3

                    ]
                )
            ]
            , justify="center")
    ]
)





header = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(html.H1("公共福利資訊",style={"margin": "15px 0px 15px 30px"}) )
            ]
        )
    ]
)

header2 = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(html.H1("常用電話",style={"margin": "15px 0px 15px 30px"}) )
            ]
        )
    ]
)
def Welfare():
    layout = html.Div([
        nav,
        header,
        layout_columns_cards,
        header2,
        INFOCARD,
        footer
    ])
    return layout


