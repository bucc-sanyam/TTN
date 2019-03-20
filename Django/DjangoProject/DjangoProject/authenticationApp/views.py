from django.contrib import admin, auth
from django.http import HttpResponse
from django.shortcuts import render


def authenticate(request):
    if request.user.is_superuser:
        return HttpResponse(request.user.__str__() + " is a super user.")
    elif request.user.is_staff:
        return HttpResponse(request.user.__str__() + " is a staff user.")
    else:
        return HttpResponse(request.user.__str__() + " is neither a super nor a staff user.")


def logout(request):
    user = request.user.__str__()
    auth.logout(request)
    return HttpResponse(user + " has been logged out.")
