from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class index(View):
    greeting = "Good Day"

    def get(self, request):
        return HttpResponse(self.greeting)


class morning_greeting(index):
    greeting = "Good Morning!"


class sessioncount(View):
    count = 0

    def get(self, request):
        my_count = request.session.get('my_count', 0)
        my_count = my_count + 1
        request.session['my_count'] = self.count = my_count
        request.session.set_expiry(300)
        return HttpResponse(str(self.count) + " and the Expiry age : " + request.session.get_expiry_age().__str__())
