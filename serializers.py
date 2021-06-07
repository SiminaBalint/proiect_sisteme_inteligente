from rest_framework import serializers
from .models import Weather


class WeatherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ['airTemperature', 'humidity', 'precipitation', 'visibility',
                  'waveDirection', 'waveHeight', 'windDirection', 'windSpeed',
                  'waterTemperature', 'cloudCover', 'wavePeriod', 'windWavePeriod']
