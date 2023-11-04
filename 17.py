# Define the risk weights for unsafe streets
risk_weights = {
    '17TH ST': 8133,
    'NOE ST': 3163,
    'DUBOCE AV': 0,
    'CASTRO ST': 6777,
    'SANCHEZ ST': 0
}

# Define the routes and their corresponding streets
routes = {
    1: ['17TH ST', 'NOE ST', 'DUBOCE AV'],
    2: ['17TH ST', 'NOE ST', 'CASTRO ST', 'SANCHEZ ST', 'DUBOCE AV'],
    3: ['DUBOCE AV', 'SANCHEZ ST', 'NOE ST', '17TH ST']
}

# Define the risk of each route
route_risks = {}
for route, streets in routes.items():
    risk = 0
    for street in streets:
        if street in risk_weights:
            risk += risk_weights[street]
    route_risks[route] = risk

# Find the safest route
safest_route = min(route_risks, key=route_risks.get)

# Print the risk of each route and the safest route
print("Route Risks:", route_risks)
print("Safest Route:", safest_route)
