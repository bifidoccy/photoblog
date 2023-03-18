from django import template
from gallery.models import *

register = template.Library()

@register.inclusion_tag('gallery/include/tags/slider_tag.html')
def get_slider():
	photos = GalleryPhoto.objects.all()
	return {'photos': photos}