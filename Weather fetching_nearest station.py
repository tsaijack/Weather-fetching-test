from requests import get
import json
from pprint import pprint
from haversine import haversine

stations = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/'

sunshine_lat = 24.790170
sunshine_lon = 120.968113

all_stations = get(stations).json()['items']

def find_closest():

    smallest = 20036 #longest distance between two points on Earth's surface.

    for station in all_stations:
        #get position of station
        station_lon = station['weather_stn_long']
        station_lat = station['weather_stn_lat']
        #calculate distance
        distance = haversine(sunshine_lon, sunshine_lat, station_lon, station_lat)
        # print(distance)
        
        if distance < smallest:
            smallest = distance
            closest_station_id = station['weather_stn_id']
            closest_station_long = station['weather_stn_long']
            closest_station_lat = station['weather_stn_lat']
            closest_station_pos = [closest_station_lat, closest_station_long]
    return closest_station_id

closest_stn = find_closest()
weather = weather + str(closest_stn) #convert id from int into str, append it at the end of url
my_weather = get(weather).json()['items']
pprint(my_weather)

            
