from datetime import datetime
from random import randint
from first.models import History
from django.shortcuts import render

def get_request(request):
    context = {}
    if int(request.GET.get('v1', 0)) > 60:
        a = int(request.GET.get('v1', 0))
        b = int(request.GET.get('v2', 0))
        context['a'] = a
        context['b'] = b
    else:
        a = randint(86, 93)
        b = 0
    record = History(
        date=datetime.now(),
        first=a,
        second=b,
    )

    record.save()
    records = History.objects.order_by('-date')
    context['history'] = records

    return render(request, 'get_request.html', context)

def history(request):
    context = {}
    records = History.objects.order_by('-date')
    context['history'] = records

    return render(request, 'history.html', context)
