from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.CustomerFeedbackListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.CustomerFeedbackDetailView.as_view(), name='detail'),
]
