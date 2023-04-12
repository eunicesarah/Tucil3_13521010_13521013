import folium
import googlemaps
import numpy as np
import webbrowser
from folium.plugins import MarkerCluster

api_key = "AIzaSyB5UAh67qqEWkt8i2VH6AMD3KJgIdx4vNI"
gmaps = googlemaps.Client(key=api_key)

def build_graph(names, latitudes, longitudes):
    n = len(names)
    graph = np.zeros((n, n))
    coordinates = []

    for i in range(n):
        coordinates.append([latitudes[i], longitudes[i]])

    for i in range(n):
        for j in range(n):
            if i != j and graph[i][j] == 0:
                distance = gmaps.distance_matrix((coordinates[i]), (coordinates[j]))['rows'][0]['elements'][0]['distance']['value']
                graph[i][j] = distance
                graph[j][i] = distance

    return names, graph, coordinates

def on_click(event):
    global latitudes, longitudes, names, nodes, coordinates
    lat, lng = event.latlng
    result = gmaps.reverse_geocode((lat, lng))
    name = result[0]['formatted_address']
    print(name)
    nodes.append(name)
    names.append(name)
    coordinates.append([lat, lng])
    latitudes.append(lat)
    longitudes.append(lng)
    folium.Marker([lat, lng], tooltip=name).add_to(m)

m = folium.Map(location=[-6.974966142193127, 107.61136450689669], zoom_start=13)

folium.Marker([-6.974966142193127, 107.61136450689669], tooltip='Click on the map').add_to(m)

latitudes = []
longitudes = []
names = []
nodes = []
coordinates = []

folium.LatLngPopup().add_to(m)
MarkerCluster().add_to(m)
folium.ClickForMarker(popup='Add a location').add_to(m)

m.save('inputmap.html')
webbrowser.open('inputmap.html')

while True:
    response = input('Do you want to add another location? (y/n): ')
    if response == 'n':
        nodes, graph, coordinates = build_graph(names, latitudes, longitudes)
        print("Nodes:")
        print(nodes)
        print("Graph:")
        print(graph)
        print("Coordinates:")
        print(coordinates)
        break
    else:
        print("Click on the map to add a location")

