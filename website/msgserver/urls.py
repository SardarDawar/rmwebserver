from django.urls import path
from .views import *

urlpatterns = [
        path("",getJson , name = "getJson"),
        path("msgserver/get/<int:key>/",detail),
        path("create/",create , name = "create"),
        path("update/<int:key>/",update , name = "update"),


        ]
