from requests import get
import json
from pprint import pprint

url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations' #data url to fetch
stations = get(url).json()['items'] #get from requests. teanslate into python dictionaries using json



