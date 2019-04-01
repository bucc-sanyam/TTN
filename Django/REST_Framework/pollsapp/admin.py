from django.contrib import admin

# Register your models here.
from pollsapp.models import Questions, Choices

admin.site.register(Questions)
admin.site.register(Choices)