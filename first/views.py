from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from random import randint
# Create your views here.
from first.models import CalcHistory


def index_page(request):
    context = {}
    context['author'] = 'Andrew'
    context['year'] = 2021
    context['pages'] = 1
    return render(request, 'index.html', context)


def current_date(request):
    context = {}
    context['date'] = datetime.now()
    context['numbers'] = [10, 20, 30, 40]
    return render(request, 'date.html', context)



def calc_page(request):
    context = {}
    if int(request.GET.get('v1', 0)) > 60:
        a = int(request.GET.get('v1', 0))
        b = int(request.GET.get('v2', 0))
        context['a'] = a
        context['b'] = b
    else:
        a = randint(86, 93)
        b = 0
    record = CalcHistory(
        date=datetime.now(),
        first=a,
        second=b,
    )

    record.save()
    records = CalcHistory.objects.order_by('-date')
    context['history'] = records

    return render(request, 'calculator.html', context)
