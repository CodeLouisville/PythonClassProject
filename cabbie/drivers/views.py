from django.shortcuts import get_object_or_404, render
from datetime import date, datetime, time
import logging

from .models import Description, Driver, Counter

logging = logging.getLogger('cabbie.drivers')

def driver_list(request):
	drivers = Driver.objects.all()
	#drivers = Driver.objects.prefetch_related('descriptions').all()
	return render(
		request, 
		'drivers/driver_list.html', 
		{'drivers': drivers, 'current_time': datetime.now()},
	)

def counter(request):
	drivers = Driver.objects.all()
	descriptions = Driver.objects.prefetch_related('descriptions').all()
	try:
		counter = Counter.objects.get(name='one')
		counter.count += 1
		counter.save()
	except:
		counter = Counter(count=1, name='one').save()

	return render(
		request, 
		'drivers/counting.html',
		{'drivers': drivers, 'current_time': datetime.now(), 'counter': counter},
	)

def test(request):
	drivers = Driver.objects.all()
	descriptions = Driver.objects.prefetch_related('descriptions').all()
	try:
		counter = Counter.objects.get(name='one')
	except:
		counter = Counter(count=0, name='one').save()

	return render(
		request, 
		'drivers/test.html',
		{'drivers': drivers, 'current_time': datetime.now(), 'counter': counter},
	)