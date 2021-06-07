from pprint import pprint

# Create your views here.
from rest_framework.generics import ListAPIView

from polls.models import Weather
from .data import getData
from .serializers import WeatherSerializers


class WeatherListView(ListAPIView):
    queryset = getData()
    serializer_class = WeatherSerializers
