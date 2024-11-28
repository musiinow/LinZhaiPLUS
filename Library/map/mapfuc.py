from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import pandas as pd

#傳入:地址(Location)
#回傳:經度(latitude) 緯度(longitude)
#如果沒有找到經緯讀則回傳none
def get_location_coordinates(location):
    geolocator = Nominatim(user_agent="geo_converter")
    try:
        location_data = geolocator.geocode(location)
        return location_data.latitude, location_data.longitude

    except:
        #print("0")
        return None
    
#傳入 房子的座標(Latitude, Longitude)
#回傳 100公尺內捷運站數量, 200公尺, 1公里
def get_nearby_station(Latitude, Longitude):
    # 載入捷運站數據
    stations = pd.read_csv('KMRT.csv')
    
    # 檢查經緯度是否有效
    if (Latitude == 'none' ) or (Longitude == 'none'):
        return 0  # 若無效則直接返回 0

    # 初始化距離計數
    house_coords = (Latitude, Longitude)
    nearby_stations100m = 0
    nearby_stations500m = 0
    nearby_stations1km = 0
    # 遍歷每個捷運站
    for _, station in stations.iterrows():
        station_coords = (station['Latitude'], station['Longitude'])
        distance = geodesic(house_coords, station_coords).kilometers

        if distance <= 0.1:  # 距離小於或等於 100 公尺
            nearby_stations100m += 1
        if distance <= 0.5:  # 距離小於或等於 500 公尺
            nearby_stations500m += 1
        if distance <= 1:  # 距離小於或等於 1000 公尺
            nearby_stations1km += 1
        
    return nearby_stations100m, nearby_stations500m, nearby_stations1km

def get_nearby_station(Latitude, Longitude):
    # 載入全台數據
    school = pd.read_csv('KMRT.csv')
    
    # 檢查經緯度是否有效
    if (Latitude == 'none' ) or (Longitude == 'none'):
        return 0  # 若無效則直接返回 0

    # 初始化距離計數
    house_coords = (Latitude, Longitude)
    nearby_stations100m = 0
    nearby_stations500m = 0
    nearby_stations1km = 0
    # 遍歷每個捷運站
    for _, station in stations.iterrows():
        station_coords = (station['Latitude'], station['Longitude'])
        distance = geodesic(house_coords, station_coords).kilometers
        
        if distance <= 0.1:  # 距離小於或等於 100 公尺
            nearby_stations100m += 1
        if distance <= 0.5:  # 距離小於或等於 500 公尺
            nearby_stations500m += 1
        if distance <= 1:  # 距離小於或等於 1000 公尺
            nearby_stations1km += 1
        
    return nearby_stations100m, nearby_stations500m, nearby_stations1km