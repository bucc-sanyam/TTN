import datetime
import os

from django.http import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt
import json


def hellouser(request):
    context_data = {'name': "Sanyam", 'footer': 'footer'}
    return TemplateResponse(request, 'hello.html', context=context_data)


def daytime(request, time):
    """ Function to print various actions """

    if 12 > time >= 6:
        return render(request, 'hello.html', {'greet': "Good Morning!"})
    elif 18 > time >= 12:
        return render(request, 'hello.html', {'greet': "Good Afternoon!"})
    elif 24 > time >= 18:
        return render(request, 'hello.html', {'greet': "Good Night!"})
    else:
        return render(request, 'hello.html', {'greet': "Go to bed!!"})


def home(request):
    """ Function to print the time of the day (default timezone set to India) """

    timenow = datetime.datetime.now()
    if timenow.hour >= 12:
        return HttpResponse("Good Evening!")
    else:
        return HttpResponse("Good Morning!")


@csrf_exempt
def finput(request):
    if request.method == 'POST':
        json_data = request.body.decode("utf-8")
        data = json.loads(json_data)
        fileName = data['file_name']
        write_content = data['content']

        with open(fileName + ".txt", "w+") as file:
            file.write(write_content)

    return HttpResponse("Thanks")


def foutput(request, fileName):
    with open(fileName + ".txt", "r") as file:
        read_content = file.read()
    return HttpResponse(read_content)


@csrf_exempt
def fupdate(request, fileName):
    if request.method == 'POST':
        json_data = request.body.decode("utf-8")
        data = json.loads(json_data)
        write_content = data['content']
        with open(fileName + ".txt", "a") as file:
            file.write(write_content)

    return HttpResponse("Updated")


def delfile(request, fileName):
    os.remove(fileName + ".txt")
    return HttpResponse("File deleted.")
