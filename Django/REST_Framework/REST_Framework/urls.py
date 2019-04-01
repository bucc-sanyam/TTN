from django.contrib import admin
from django.urls import path
from pollsapp.views import question_list,question_detail,choices_list, choices_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('question/',question_list),
    path('question/<int:pk>',question_detail),
    path('choices/',choices_list),
    path('choices/<int:pk>',choices_detail)
]