from django.db import models

class GalleryPhoto(models.Model):
	img = models.ImageField(upload_to='gallery/')
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']



class Gallery(models.Model):
	images = models.ManyToManyField(GalleryPhoto)
	name = models.CharField(max_length=100)
	create_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']