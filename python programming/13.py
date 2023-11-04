import folium
import networkx as nx
from geopy.distance import distance

# Define the two points
point_a = (40.7128, -74.0060)  # New York City
point_b = (51.5074, -0.1278)   # London

# Calculate the distance between the two points in kilometers
distance_km = distance(point_a, point_b).km

# Create a map centered at the first point
map_center = point_a
map = folium.Map(location=map_center, zoom_start=3)

# Create a marker for each point and add them to the map
folium.Marker(location=point_a, tooltip="Point A").add_to(map)
folium.Marker(location=point_b, tooltip="Point B").add_to(map)

# Create a graph with the two points as nodes and the distance between them as the edge weight
G = nx.Graph()
G.add_node("A", pos=point_a)
G.add_node("B", pos=point_b)
G.add_edge("A", "B", weight=distance_km)

# Calculate the shortest path between the two points
shortest_path = nx.shortest_path(G, "A", "B", weight="weight")

# Create a PolyLine object to connect the markers along the shortest path
polyline = folium.PolyLine(
    locations=[G.nodes[node]["pos"] for node in shortest_path],
    color="red",
    weight=5
)

# Add the PolyLine to the map
polyline.add_to(map)

# Display the map on the screen
map
