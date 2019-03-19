from django.urls import path
from .views import *


urlpatterns = [
    path('display/', display),
    path('index/', index)
]