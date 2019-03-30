from django.contrib import admin
from django.urls import path
from cbvapp.views import StudentGetPost, GreetUser, StudentUpdate, StudentDelete, StudentRetrieve, StudentList
urlpatterns = [
    path('greet/', GreetUser, name='greet-user'),
    path('student/<int:pk>', StudentRetrieve.as_view()),
    path('student/<int:pk>/update', StudentUpdate.as_view()),
    path('student/<int:pk>/delete', StudentDelete.as_view()),
    path('student/add', StudentGetPost.as_view()),
    path('student/', StudentList.as_view()),
    path('admin/', admin.site.urls),
]