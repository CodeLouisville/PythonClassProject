from django.conf.urls import url

from .views import subscribe, unsubscribe

urlpatterns = [
    url(r'signup/$', subscribe, name="subscribe"),
    url(r'unsubscribe/$', unsubscribe, name="unsubscribe"),
]