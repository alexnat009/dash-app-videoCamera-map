#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

px.defaults.color_continuous_scale = px.colors.sequential.Peach
fig = px.bar(pd.read_excel('./dataset/wholeData/data.xlsx', sheet_name="Sheet1"), x="წელი", y="რაოდენობა", color="რაოდენობა")
fig.update_layout(xaxis_tickformat='d', font_family="BPG Nino Mtavruli", title_text="ვიდეოკამერების რაოდენობა წლების მიხედვით")
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    html.Div("აირჩიეთ წელი", style={"text-align": "center", "margin-top": "10px", "font-weight": "bold"}),
    dcc.Slider(
        min=2019, max=2021, step=1,
        marks={i: str(i) for i in range(2019, 2022)},
        value=2019,
        id="my-slider"),
    html.Div("აირჩიეთ კამერის ტიპი", style={"text-align": "center", "margin-top": "10px", "font-weight": "bold"}),
    dcc.Dropdown(
        id="dropdown",
        options=["ნომრის ამომცნობი ვიდეოკამერები", "ზოგადი ხედვის ვიდეოკამერები", "წერტილოვანი რადარი"],
        value="ნომრის ამომცნობი ვიდეოკამერები",
        clearable=False,
        style={"margin-bottom": "10px", "align-items": "center", "justify-content": "center", "text-align-last": "center"}
    ),
    html.Div([
        dcc.Graph(id="typeGraph"),
        html.Div(id="graphInfo", children=["fasd"]),
        html.Iframe(id="map", style={"width": "100%", "height": "700px", "border": "none"}), ]),
    html.Div([
        dcc.Graph(id="yearlyGraph", figure=fig),
        html.Div(
            """მოცემულ ბაზაში თვალნათლივ ჩანს, რომ 2019 წელს განთავსდა ყველაზე კამერა, მთლიანი რაოდენობის 74%. აღსანიშნავია ფაქტი, რომ კამერების დიდი რაოდენობა ყოველ წელს თავსდებოდა საქართველოს ადმინისტრაციული,
             მნიშვნელოვანი სამრეწველო და კულტურული ცენტრების დამაკავშირებელ გზებზე და მაგისტრალებზე, რაც უფრო უსაფრთხოს ხდის მათ შორის გადაადგილებას. """,
            style={"background-color": "#FBD0AD", "padding": "20px", "border-radius": "7px", "text-align": "justify"}, )
    ], style={"display": "flex", "height": "450px", "width": "100%", "justify-content": "space-between", "align-items": "center"}, id="goingTop"),
    html.Div(["წყარო: https://info.police.ge/page?id=305", html.P(["https://askgov.ge, ", "OpenStreetMap"])])
], style={"text-align": "center", "margin-top": "10px"})
server = app.server


@app.callback(

    Output("dropdown", "options"),
    Output("graphInfo", "children"),
    Input("my-slider", "value"))
def update_year(year):
    types = ["ნომრის ამომცნობი ვიდეოკამერები", "ზოგადი ხედვის ვიდეოკამერები",
             "წერტილოვანი რადარი"] if year != 2021 else ["ნომრის ამომცნობი ვიდეოკამერები", "ზოგადი ხედვის ვიდეოკამერები"]
    if year == 2019:
        return types, html.Div("""2019 წელს აღინიშნება რამდენიმე საინტერესო მონაცემი, 
                კერძოდ, ნომრის ამომცნობი ვიდეოკამერების მაქსიმალური რაოდენობა მარნეულში, რომელიც დაკავშირებულია
                მარნეულის აქტიურ სატრანზიტო-სატვირთო დანიშნულებასთან. მსგავსი სიტუაციაა ბათუმშიც, რომელსაც კიდევ
                ემატება სასაზღვრო ქალაქის და აქტიური საკურორტო წერტილის სტატუსი. ზოგადი ხედვის ვიდეოკამერები
                მოსალოდნელად არის განაწილებული, მათი დიდი რაოდენობა თავმოყრილია დიდ დასახლებულ პუნქტებში.
                აღსანიშნავია წერტილოვანი რადარების რაოდენობა თბილისში, რომელიც მაქსიმალურია იმერეთის მხარესთან ერთად.""",
                               style={"background-color": "#FBD0AD", "padding": "20px", "border-radius": "7px", "text-align": "justify", "margin-bottom": "10px"})
    if year == 2020:
        return types, html.Div("""აღინიშნება საკმაორდ დიდი ამპლიტუდა 2019 წლიდან 2020 წელზე. დრამატულად იკლო ახალი კამერების
                რაოდენობამ, კონკრეტულად კი იკლი 2220 ერთეულით. მოცემულ წელს ნომრის ამომცნობი ვიდეოკამერებში ლიდერობს თბილისი,
                შემდგომ ქუთაისი. ზოგადი ხედვის ვიდეოკამერებში კი ფოთი, რაც მსგავსად მარნეულისა, შეიძლება დავუკავშიროთ ფოთის 
                სატრანზიტო-სატვირთო დანიშნულებას. ასვე აღინიშნება მცირე, მაგრამ კამერების დამატება სამცხე-ჯავახეთის და კახეთის ტერიტორიაზე, რაც გზის რეაბილიტაციას შეიძლება დავუკავშიროთ.""",
                               style={"background-color": "#FBD0AD", "padding": "20px", "border-radius": "7px", "text-align": "justify", "margin-bottom": "10px"})
    if year == 2021:
        return types, html.Div("""2021 წელს საინტერესოა რამდენიმე ფაქტი, კერძოდ, ზოგადი ხევის ვიდეოკამერების უმეტესობის დამატება თბილისში, რომლის მიზეზიც შეიძლება იყოს აქტიური ურბანიზაციის პროცესი.
         ასევე საყურადღებოა ახალი წერტილოვანი რადარების არარსებობა, რომლის მიზეზიც ამ ეტაპზე გაუგებარია. ხოლო დამატებული ნომრის ამომცნობი ვიდეოკამერების  რაოდენობაში ლიდერობს ქუთაისი, რაც მსგავსად თბილისისა შეიძლება
         მისი ურბანიზაციის მაღალი დონიდან გამომდინარეობდეს.""",
                               style={"background-color": "#FBD0AD", "padding": "20px", "border-radius": "7px", "text-align": "justify", "margin-bottom": "10px"})


@app.callback(
    Output("typeGraph", "figure"),
    Output("map", "srcDoc"),
    Input("my-slider", "value"),
    Input("dropdown", "value"))
def update_year(year, cameraType):
    camera = "carCamera"
    if cameraType == "ზოგადი ხედვის ვიდეოკამერები":
        camera = "generalView"
    if cameraType == "წერტილოვანი რადარი":
        camera = "pointRadar"
    if year == 2021 and cameraType == "":
        camera = "carCamera"

    df = pd.read_excel(f'./dataset/{year}/year{year}.xlsx', sheet_name="Sheet1")
    fig = px.bar(df[df[["ქალაქი", "გრძედი", "განედი", cameraType]][cameraType] != 0], x="ქალაქი", y=cameraType,
                 barmode="group", color=cameraType)
    fig.update_xaxes(tickangle=45)
    fig.update_layout(font_family="BPG Nino Mtavruli", title_text="ვიდეოკამერების განაწილება დასახლებულ პუნქტებში")
    return fig, open(f'./website/{year}/{camera}.html', 'r', encoding="utf-8").read()


app.run_server(port=33507)
