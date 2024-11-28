import pandas as pd
from mapfuc import get_location_coordinates

#讀取檔案並將Location中無用資訊移除
df = pd.read_csv('House_Rent_Info.csv')
df['Location'] = df['Location'].apply(lambda x: x.split('/')[0].strip() if isinstance(x, str) else x)


latitudes = []
longitudes = []

#遍歷檔案中的Location 回傳座標
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
