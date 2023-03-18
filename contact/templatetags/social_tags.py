from django import template
from contact.models import *

register = template.Library()

@register.simple_tag()
def get_philosophy():
	return OurPhilosophy.objects.last()

@register.simple_tag()
def get_about():
	return About.objects.last()

@register.simple_tag()
def get_socials():
	return Social.objects.all()