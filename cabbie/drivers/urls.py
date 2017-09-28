from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'test/', views.test, name='test'),
    url(r'counter/', views.counter, name='counter'),
    url(r'^$', views.driver_list, name='list'),
]