from django import template
from drivers.models import Counter

register = template.Library()

@register.simple_tag
def every_five():
	''' This returns a special message for every 5 clicks '''
	if Counter.objects.get(name='one').count % 10 == 0:
		return 'Ten clicks in'
	elif Counter.objects.get(name='one').count % 5 == 0:
		return 'Five clicks in'
	else:
		return ''

@register.inclusion_tag('drivers/success.html')
def success_tag():
	''' This returns a special message for every 5 clicks '''
	if Counter.objects.get(name='one').count > 20:
		return {'display':True, 'almostthere':False}
	elif Counter.objects.get(name='one').count > 15:
		return {'display':False, 'almostthere':True}
	else:
		return {'display':False, 'almostthere':False}

@register.filter('times')
def times(num):
	return range(num)