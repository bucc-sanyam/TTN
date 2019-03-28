from .views import *
from django.urls import path
urlpatterns = [
    path('home/', home, name="home"),
    path('daytime/<int:time>/', daytime, name='daytime'),
    path('file/input/', finput, name='finput'),
    path('file/output/<str:fileName>', foutput, name="foutput"),
    path('file/update/<str:fileName>', fupdate, name='fupdate'),
    path('file/delete/<str:fileName>', delfile, name = 'delfile'),
    path('hellouser/<str:username>',hellouser, name= 'hellouser')
]
