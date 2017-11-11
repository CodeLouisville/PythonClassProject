from django.http import HttpResponse
from django.shortcuts import render

from .models import Subscriber
from .forms import NewsletterSubscribeForm

def subscribe(request):
    form = NewsletterSubscribeForm(request.POST or None)

    if form.is_valid():
        #don't send it to the database just yet
        instance = form.save(commit=False)
        if Subscriber.objects.filter(email=instance.email).exists():
            print("Congratulations! You're already subscribed")
        else:
            instance.save()

    context = {
        'form': form,
    }
    template = "newsletters/subscribe.html"
        
    return render(request, template, context)


def unsubscribe(request):
    form = NewsletterSubscribeForm(request.POST or None)

    if form.is_valid():
        #don't send it to the database just yet
        instance = form.save(commit=False)
        if Subscriber.objects.filter(email=instance.email).exists():
            Subscriber.objects.filter(email=instance.email).delete()
        else:
            print("Email not found.")

    context = {
        'form': form,
    }
    template = "newsletters/unsubscribe.html"

    return render(request, template, context)
