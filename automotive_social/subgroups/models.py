from django.db import models
from django.urls import reverse
# Create your models here.

# to connect a subgroup to an actual Group
from groups.models import Group

# slugify allows us to remove any characters that arent alphanumeric, underscores, or hyphens
from django.utils.text import slugify

# connect post to current user
from django.contrib.auth import get_user_model
User = get_user_model()

class SubGroup(models.Model):
	name = models.CharField(max_length=50)
	slug = models.SlugField(allow_unicode=True, blank=True)
	description = models.TextField(blank=True, default='')
	created_at = models.DateTimeField(auto_now=True)


	user = models.ForeignKey(User, related_name='subgroups',on_delete=models.CASCADE)
	group = models.ForeignKey(Group, related_name='subgroups', null=True, blank=True,on_delete=models.CASCADE)


	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super().save(*args, **kwargs)


	# for the createview to redirect once form is submitted, 
	# redirects back to subgroup page you just created a new post on
	def get_absolute_url(self):
		return reverse('subgroups:all', kwargs={'slug':self.group.slug})


	class Meta:
		ordering = ['-created_at']
