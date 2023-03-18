from django.urls import path
from . import views
from django.views.decorators.cache import cache_page


urlpatterns = [
	path('contact/', cache_page(60 * 15)(views.ContactView.as_view()), name='contact'),
	path('feedback/', views.CreateComment.as_view(), name='feedback')
]