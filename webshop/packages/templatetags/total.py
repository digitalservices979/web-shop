from django import template

register = template.Library()

def total(cantidad,precio):
	return round((cantidad*precio),2)

register.filter('total',total)