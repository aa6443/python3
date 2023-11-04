import osmnx as ox
import networkx as nx
import folium
from folium.plugins import HeatMap
start_point = (lat1, lon1)
end_point = (lat2, lon2)


graph = ox.graph_from_point(start_point, distance=500, network_type='drive')

start_node = ox.get_nearest_node(graph, start_point)
end_node = ox.get_nearest_node(graph, end_point)
shortest_path = nx.shortest_path(graph, start_node, end_node, weight='length')

m = folium.Map(location=start_point, zoom_start=15)

path_coordinates = [[graph.nodes[node]['y'], graph.nodes[node]['x']] for node in shortest_path]
folium.PolyLine(path_coordinates, color='red', weight=5, opacity=0.7).add_to(m)

m


