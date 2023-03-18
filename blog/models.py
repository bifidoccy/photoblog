from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse


class Category(MPTTModel):
	name = models.CharField(max_length=40, unique=True)
	slug = models.SlugField(max_length=100)
	parent = TreeForeignKey(
		'self',
		related_name='children',
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
	)

	class MPTTMeta:
		order_insertion_by = ['name']

	def __str__(self):
		return self.name


class Tags(models.Model):
	name = models.CharField(max_length=50)
	slug = models.SlugField(max_length=100)

	def __str__(self):
		return self.name



class Article(models.Model):
	category = models.ManyToManyField(
		Category,
		related_name='article'
	)
	create_at = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(
		User,
		related_name='articles',
		on_delete=models.CASCADE
	)
	tags = models.ManyToManyField(
		Tags,
		related_name='article'
	)
	title = models.CharField(max_length=150)
	image = models.ImageField(upload_to='articles/')
	gallery_img1 = models.ImageField(upload_to='articles/gallery_img', default='')
	gallery_img2 = models.ImageField(upload_to='articles/gallery_img', default='')
	text = models.TextField()
	slug = models.SlugField(max_length=200, default='', unique=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		context = self.category.all()
		cat_slug = str(context[0]).lower()
		return reverse('article_detail', kwargs={'slug': cat_slug, 'article_slug': self.slug})


class Reply(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField(max_length=100)
	comment = models.TextField(max_length=1000)
	create_at = models.DateTimeField(default=timezone.now)
	article = models.ForeignKey(
		Article,
		on_delete=models.CASCADE,
		related_name='reply'
	)

