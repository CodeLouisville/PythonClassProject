from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ReviewListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.ReviewDetailView.as_view(), name='detail'),
    url(r'^create/$', views.ReviewCreateView.as_view(), name='create'),
    url(r'^edit/(?P<pk>\d+)/$', views.ReviewUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', views.ReviewDeleteView.as_view(), name='delete'),
]
