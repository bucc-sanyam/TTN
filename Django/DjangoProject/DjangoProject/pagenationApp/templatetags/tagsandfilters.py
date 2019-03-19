import math

from django import template
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt

register = template.Library()

def capital(value):
    return value.capitalize()





@register.simple_tag(name="square")
def calculate_square(value):
    return math.pow(value, 2)

register.filter('capital',capital)