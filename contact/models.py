from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

class About(models.Model):
	name = models.CharField(max_length=100, default='About')
	main_about = RichTextField(max_length=500)
	footer_about = models.TextField(max_length=300)

	def __str__(self):
		return self.name

class OurPhilosophy(models.Model):
	name = models.CharField(max_length=100, default='Our Philosophy')
	par1 = models.TextField()
	par2 = models.TextField()

	def __str__(self):
		return self.name

class ContactModel(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField(max_length=100)
	subject = models.CharField(max_length=70)
	message = models.TextField(max_length=1000)
	create_at = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return f'{self.name} - {self.email}'

class EmbedMap(models.Model):
	source = models.URLField(max_length=600)

class Social(models.Model):
	name = models.CharField(max_length=50)
	url = models.URLField()
	icon = models.ImageField(upload_to='social/')

	def __str__(self):
		return self.name