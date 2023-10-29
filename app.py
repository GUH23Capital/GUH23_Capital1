from flask import Flask, render_template
import folium
import pandas as pd
from geopy.geocoders import Nominatim

app = Flask(__name__)

# Load data from the CSV file
def load_data():
    return pd.read_csv("transactions_with_details.csv")

def filter_data(name, m):
    df = load_data()
    # Create a map centered on the city of York
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(f"{name}, UK")
    if location:
        map_center = [location.latitude, location.longitude]
    else:
        # Fallback coordinates if geocoding fails
        map_center = [53.9590, -1.0815]

    m = folium.Map(location=[map_center[0], map_center[1]], zoom_start=10)


    # Add markers for points in the city
    for index, row in df.iterrows():
        if isinstance(row['City'], str) and row['City'].lower() == name.lower():
            popup_text = f"<b>{row['Merchant Name']}</b><br>Timestamp: {row['Timestamp']}<br>Road:{row['Road']}<br>City: {row['City']}<br>County: {row['County']}"
            folium.Marker(
                location=[row['Latitude'], row['Longitude']],
                popup=folium.Popup(popup_text, max_width=200),
            ).add_to(m)

    # Save the map to an HTML file (optional)
    m.save("searchedMap.html")



# Your Flask routes and logic go here
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sfaf')
def sfaf():
    return render_template('sfaf.html')

@app.route('/map')
def map():
    df = load_data()
    # Create a base map
    m = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=6)

    # Add markers for each latitude and longitude
    for index, row in df.iterrows():
        popup_text = f"<b>{row['Merchant Name']}</b><br>Timestamp: {row['Timestamp']}<br>Road:{row['Road']}<br>City: {row['City']}<br>County: {row['County']}"
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=folium.Popup(popup_text, max_width=200),
        ).add_to(m)

    # Save the map to an HTML file (optional)
    m.save("map.html")
    return render_template('map.html')

if __name__ == '__main__':
    app.run(debug=True)
