from django.urls import path
from authenticationApp.views import *

urlpatterns = [
    path('authenticate/', authenticate),
    path('logout/', logout),
    ]



