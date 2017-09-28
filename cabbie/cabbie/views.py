from django.shortcuts import get_object_or_404, render
from datetime import date, datetime, time

def home(request):
	return render(
		request, 
		'home.html',
		{'current_time': datetime.now()},
	)