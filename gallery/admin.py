from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

@admin.register(GalleryPhoto)
class PhotoAdmin(admin.ModelAdmin):
	list_display = ['name', 'get_image']
	readonly_fiels = ['get_image',]

	def get_image(self, obj):
		return mark_safe(f'<img src={obj.img.url} width=70px>')

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
	list_display = ['name', 'create_at']

