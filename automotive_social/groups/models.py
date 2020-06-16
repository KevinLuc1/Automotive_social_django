from django.db import models
# slugify allows us to remove any characters that arent alphanumeric, underscores, or hyphens
from django.utils.text import slugify
# returns the user model that is currently active in this project
from django.contrib.auth import get_user_model
User = get_user_model()

from django.urls import reverse



class Group(models.Model):
	name = models.CharField(max_length=50, unique=True)
	slug = models.SlugField(allow_unicode=True, unique=True, blank=True)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super().save(*args, **kwargs)

	# def get_absolute_url(self):
	# 	return reverse('groups:single', kwargs={'slug':self.slug})

	class Meta:
		ordering = ['name']
