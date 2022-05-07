import folium
from branca.element import Figure
import pandas as pd

years = [2019, 2020, 2021]
for year in years:
    df = pd.read_excel(f'./dataset/{year}/year{year}.xlsx', sheet_name="Sheet1")
    cameraTypes = [["ნომრის ამომცნობი ვიდეოკამერები", "carCamera"],
                   ["ზოგადი ხედვის ვიდეოკამერები", "generalView"],
                   ["წერტილოვანი რადარი", "pointRadar"]] if year != 2021 else [["ნომრის ამომცნობი ვიდეოკამერები", "carCamera"], ["ზოგადი ხედვის ვიდეოკამერები", "generalView"]]
    for cameraType in cameraTypes:
        fig = Figure(width=600, height=400)
        georgiaMap = folium.Map(location=[42.047662, 43.622645],
                                min_lon=39.423066,
                                max_lon=46.920744,
                                min_lat=43.674230,
                                max_lat=41.027986,
                                max_bounds=True,
                                zoom_start=8,
                                min_zoom=8,
                                max_zoom=10,
                                width='100%',
                                height='80%',
                                zoom_control=True,
                                prefer_canvas=True,
                                )
        for _, city in df.iterrows():
            if city[cameraType[0]] != 0:
                radi = float(city[cameraType[0]]) * 80
                if city[cameraType[0]] < 10:
                    radi = float(city[cameraType[0]]) * 250
                if city[cameraType[0]] > 100:
                    radi = 9000
                folium.Circle(location=(city["გრძედი"], city["განედი"]),
                              tooltip=str(f'{city["ქალაქი"].strip()}:{city[cameraType[0]]}'),
                              radius=radi,
                              color='crimson',
                              fill=True,
                              fill_color='crimson').add_to(georgiaMap)
        georgiaMap.save(f'./website/{year}/{cameraType[1]}.html')
