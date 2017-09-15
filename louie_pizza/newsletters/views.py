from django.http import HttpResponse
from django.shortcuts import render

from .models import Subscriber

def subscribe(request):
    subscribers = Subscriber.objects.all()
    return render(request, 'newsletters/subscribe.html', {'subscribers': subscribers})
