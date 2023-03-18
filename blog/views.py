from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from blog.models import *
from .forms import ReplyForm
from django.db.models import Prefetch

class HomeView(ListView):
	model = Article
	template_name = 'blog/home.html'
	paginate_by = 3

class ArticleListView(ListView):
	model = Article
	context_object_name = 'article_list'

	def get_queryset(self):
		self_slug = self.kwargs.get('slug')
		return Article.objects.filter(category__slug=self_slug).prefetch_related('category').select_related('author')

class ArticleListAllView(ListView):
	model = Article
	context_object_name = 'article_list'
	template_name = 'blog/article_list.html'

	def get_queryset(self):
		return Article.objects.prefetch_related('category', 'tags').select_related('author')


class ArticleDetailView(DetailView):
	model = Article
	slug_url_kwarg = 'article_slug'
	context_object_name = 'article'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['form'] = ReplyForm()
		return context

	def get_queryset(self):
		slug = self.model.slug
		return Article.objects.select_related('author').filter(slug=self.kwargs.get('article_slug'))

class CreateReply(CreateView):
	model = Reply
	form_class = ReplyForm

	def form_valid(self, form):
		form.instance.article_id = self.kwargs.get('pk')
		return super().form_valid(form)

	def get_success_url(self):
		return self.object.article.get_absolute_url()

class GalleryView(ListView):
	model = Article
	template_name = 'blog/gallery.html'
	context_object_name = 'article_list'

	def get_queryset(self):
		return Article.objects.prefetch_related('category').order_by('-id')
