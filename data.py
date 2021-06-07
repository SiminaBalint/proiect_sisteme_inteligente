from datetime import timezone

import arrow
import requests
import requests
from django.utils.datetime_safe import datetime

from polls.models import Weather

unixData = 1546326131
start = datetime.fromtimestamp(unixData, tz=timezone.utc)

# Get last hour of today
end = datetime.now(tz=timezone.utc)




response = requests.get(
    'https://api.stormglass.io/v2/weather/point',
    params={
        'lat': 58.7984,
        'lng': 17.8081,
        'params': ','.join(['airTemperature', 'humidity', 'precipitation', 'visibility',
                            'waveDirection', 'waveHeight',  'windDirection', 'windSpeed',
                            'waterTemperature','cloudCover','wavePeriod','windWavePeriod']),
        'start': start,
        'end': end,
        'source': 'sg'

    },
    headers={
        'Authorization': 'd3449746-c6a1-11eb-8d12-0242ac130002-d34497be-c6a1-11eb-8d12-0242ac130002'
    }
)

# Do something with response data.
json_data = response.json()
print(json_data)

def getJsonData():
    return json_data


def getData():
    for i in json_data["hours"]:
        airTemperature = i["airTemperature"]['sg']
        cloudCover = i["cloudCover"]['sg']
        humidity = i["humidity"]['sg']
        precipitation = i["precipitation"]['sg']
        visibility = i["visibility"]['sg']
        waterTemperature = i["waterTemperature"]['sg']
        waveDirection = i["waveDirection"]['sg']
        waveHeight = i["waveHeight"]['sg']
        windWavePeriod = i["windWavePeriod"]['sg']
        windDirection = i["windDirection"]['sg']
        windSpeed = i["windSpeed"]['sg']
        wavePeriod = i["wavePeriod"]['sg']
        weather = Weather(airTemperature, cloudCover, humidity, precipitation, visibility, waterTemperature,
                          waveDirection, waveHeight, windWavePeriod, windDirection, windSpeed,
                          wavePeriod)

        weather.save()
    weathers = Weather.objects.all()
    return weathers

