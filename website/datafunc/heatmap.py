import folium
from folium import plugins
from folium.plugins import HeatMap
from ..datafunc.teamstats import average_stats_against_opposition
from ..datafunc.preparation import create_dataframe, clean_dataframe

def create_average_heatmap(column):
    coords = create_dataframe("assets/coords.csv")
    stats = clean_dataframe(create_dataframe("assets/dataset.csv"))

    print(coords.to_string())

    uk_map = folium.Map(location=[51.5074, 0.1278], zoom_start=7, min_lat=49, max_lat=52, min_lon=-8, max_lon=2)

    coords["latitude"] = coords["latitude"].astype(float)
    coords["longitude"] = coords["longitude"].astype(float)

    average_stats = []
    
    for team in coords["Opposition"].tolist():
        average_stats.append(average_stats_against_opposition(stats, team, column))
    
    coords.insert(len(coords.columns), "heat", average_stats, True)
    
    heat_df = coords[["latitude", "longitude","heat"]]
    heat_df = heat_df.dropna(axis=0, subset=["latitude","longitude","heat"])
    
    heat_data = [[row["latitude"],row["longitude"],row["heat"]] for index, row in heat_df.iterrows()]

    uk_map.add_child(plugins.HeatMap(heat_data))
    uk_map.save('map.html')
