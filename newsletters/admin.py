from django.contrib import admin

from .models import Subscriber

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_subscribed',)

admin.site.register(Subscriber, SubscriberAdmin)
