from django.urls import path, re_path
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
	path('', views.HomeView.as_view(), name='home'),
	path('articles/', views.ArticleListAllView.as_view(), name='article_list_all'),
	path('gallery/', cache_page(60 * 10)(views.GalleryView.as_view()), name='gallery'),
	re_path(r'^articles/(?P<slug>\w+)/$', views.ArticleListView.as_view(), name='article_list'),
	re_path(r'^articles/(?P<slug>\w+)/(?P<article_slug>\w+)/$', views.ArticleDetailView.as_view(), name='article_detail'),
	path('reply/<int:pk>/', views.CreateReply.as_view(), name="create_reply"),
]