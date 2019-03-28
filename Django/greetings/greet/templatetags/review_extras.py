from django import template

register = template.Library()


def cut(value, arg):
    return value.replace(arg, "")


def lower(value):
    return value.lower()


@register.filter(name="lower")
def compare(value):
    if value == 'sanyam':
        return "Lower Case"
    else:
        return "Upper Case"


register.filter('cut', cut)
register.filter('lower', lower)
