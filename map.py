import folium

agencies = [
    {"name": "York-Poquoson Sheriff’s Office", "cameras": 22, "location": [37.2104, -76.3869]},
    {"name": "Chesapeake Police Department", "cameras": 44, "location": [36.7682, -76.2875]},
    {"name": "Hampton Police Division", "cameras": 54, "location": [37.0299, -76.3452]},
    {"name": "Portsmouth Police Department", "cameras": 60, "location": [36.8354, -76.2983]},
    {"name": "Newport News Police Department", "cameras": 74, "location": [37.0871, -76.4730]},
    {"name": "Norfolk Police Department", "cameras": 172, "location": [36.8508, -76.2859]},
    {"name": "Virginia Beach Police Department", "cameras": 19, "location": [36.8529, -75.9780]}  # 19 installed, 6 more in the works
]

# Initialize the map centered around Hampton Roads
map_hampton_roads = folium.Map(location=[36.85, -76.3], zoom_start=10)

# Add markers for each agency
for agency in agencies:
    folium.Marker(
        location=agency["location"],
        popup=f"{agency['name']}: {agency['cameras']} cameras",
        tooltip=agency["name"],
    ).add_to(map_hampton_roads)

# Save the map to an HTML file
map_hampton_roads.save("hampton_roads_map.html")