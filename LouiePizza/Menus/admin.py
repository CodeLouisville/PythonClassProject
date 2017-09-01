from django.contrib import admin

from .models import MenuItemType, MenuItem

admin.site.register(MenuItem)
admin.site.register(MenuItemType)
