import pdb
from django.contrib import admin

from .models import Description, Driver, Counter

class DriverAdmin(admin.ModelAdmin):
    readonly_fields = ('driver_descriptions',)
    list_display = ['last_name', 'first_name', 'email', ]

    def driver_descriptions(self, obj):
        descs = obj.descriptions.all()
        #pdb.set_trace()
        return ", ".join([d.title for d in descs]) if descs else "None"

admin.site.register(Description)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Counter)