from requests import get
import json
from pprint import pprint
#specficted stn ID in url, get weather
url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/255541'
weather = get(url).json()['items']
pprint(weather)

