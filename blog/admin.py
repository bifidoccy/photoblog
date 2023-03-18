from django.contrib import admin
from .models import *
from mptt.admin import MPTTModelAdmin

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	list_display = ['title', 'author', 'create_at', 'id']

@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
	list_display = ['name', 'email', 'create_at', 'id', 'article']

admin.site.register(Tags)
admin.site.register(Category, MPTTModelAdmin)