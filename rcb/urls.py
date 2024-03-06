from django.urls import path

from rcb.views import getResistorColorCodes 




urlpatterns = [
    # ex: /polls/
    #path("", views.index, name="index"),
    path("", getResistorColorCodes, name="getResistorColorCodes"),

    
]