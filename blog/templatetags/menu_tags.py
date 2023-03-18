from django import template
from blog.models import Article, Category, Tags
from django.db.models import Prefetch

register = template.Library()

def get_all_categories():
	return Category.objects.all()

@register.inclusion_tag('blog/include/tags/top_menu.html')
def get_categories():
	cats = get_all_categories()
	return {'list_of_cats': cats}

@register.simple_tag()
def get_last_nine_articles():
	return Article.objects.prefetch_related(Prefetch('category', queryset=Category.objects.select_related('parent'))).order_by('-id')[:9]

@register.simple_tag()
def get_last_four_articles():
	return Article.objects.prefetch_related('tags', 'category').order_by('-id')[:4]

@register.simple_tag()
def get_tags():
	return Tags.objects.all()

@register.simple_tag()
def get_last_three_articles():
	return Article.objects.prefetch_related('tags','category').order_by('-id')[:3]

@register.inclusion_tag('blog/include/tags/gallery_tag.html')
def get_gallery():
	articles = Article.objects.prefetch_related('tags', 'category').order_by('-id')[:6]
	return {'article_list': articles}
