from django.db import models
import datetime
from django.utils import timezone


class Weather(models.Model):
    airTemperature = models.FloatField(default=0)
    humidity = models.FloatField(default=0)
    precipitation = models.FloatField(default=0)
    visibility = models.FloatField(default=0)
    waveDirection = models.FloatField(default=0)
    waveHeight = models.FloatField(default=0)
    windDirection = models.FloatField(default=0)
    windSpeed = models.FloatField(default=0)
    waterTemperature = models.FloatField(default=0)
    cloudCover = models.FloatField(default=0)
    wavePeriod = models.FloatField(default=0)
    windWavePeriod = models.FloatField(default=0)

