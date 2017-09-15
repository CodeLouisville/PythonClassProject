from django.http import HttpResponse
from django.shortcuts import render

from .models import Category

import pdb

def menu(request):
    categories = Category.objects.prefetch_related('items').all()
    # Bonus points uncomment the pdb trace and in your terminal explore categories and items. 
    # Try switching .all() to values() and see what the difference is.
    #pdb.set_trace() 
    return render(request, 'menus/louiemenu.html', {"categories": categories})
