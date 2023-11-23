from django.urls import path

from rcb import views




urlpatterns = [
    # ex: /polls/
    #path("", views.index, name="index"),
    path("", views.resistor_ccodes, name="resistor_ccodes"),

    
]