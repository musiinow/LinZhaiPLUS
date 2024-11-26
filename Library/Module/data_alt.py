import pandas as pd
from geopy.geocoders import Nominatim as nom
from geopy.distance import geodesic

def get_location_coordinates(location):
    geolocator = nom(user_agent="geo_converter")
    try:
        location_data = geolocator.geocode(location)
        return location_data.latitude, location_data.longitude

    except:
        #print("0")
        return None


df = pd.read_csv('House_Rent_Info.csv')


df['Location'] = df['Location'].apply(lambda x: x.split('/')[0].strip() if isinstance(x, str) else x)


latitudes = []
longitudes = []

for location in df['Location']:
    try:
        isinstance(location, str) and location.strip()
        coords = get_location_coordinates(location)
        lat, lon = coords


    except:
        lat, lon = None, None

    latitudes.append(lat)
    longitudes.append(lon)


df['Latitude'] = latitudes
df['Longitude'] = longitudes


df.to_csv('House_Rent_Info_Alt.csv', index=False)
