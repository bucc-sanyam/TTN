from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, render


class Footer:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        return render("<p>Made by : Sanyam Gupta</p>")

