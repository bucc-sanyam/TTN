from django.urls import path

from cbvapp.views import *

urlpatterns = [
    path('index/', index.as_view()),
    path('morning/', morning_greeting.as_view()),
    path('count', sessioncount.as_view())
]