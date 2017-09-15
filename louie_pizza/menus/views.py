from django.http import HttpResponse
from django.shortcuts import render

from .models import MenuItem, MenuItemType

import pdb

def menu(request):
    categories = MenuItemType.objects.values()
    items = MenuItem.objects.values()
    # Bonus points uncomment the pdb trace and in your terminal explore categories and items. 
    # Try switching .all() to values() and see what the difference is.
    # pdb.set_trace() 
    return render(request, 'menus/louiemenu.html', {"categories": categories, "items": items})
