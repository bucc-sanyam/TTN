import random

from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    user_list = [0, ]
    for i in range(0, 1000):
        user_list.append(random.randint(0, (i * 10)))
    page = request.GET.get('page', 1)
    paginate_by = 20
    paginator = Paginator(user_list, paginate_by)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'order.html', {'users': users})


def display(request):
    person_name = 'sanyam'
    order_list = [1234, 4567, 6789, 1472]
    order_warranty = True
    return render(request, 'order.html',
                  {"person_name": person_name, "order_list": order_list, "warranty": order_warranty})
