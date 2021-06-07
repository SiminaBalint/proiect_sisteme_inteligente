from django.contrib import admin
from django.urls import include, path

from polls.train_test import TrainTest
from polls.views import WeatherListView

urlpatterns = [
    path('', WeatherListView.as_view()),
    path('', TrainTest)
]