from django.db import models
from django.urls import reverse
from django.conf import settings
# Create your models here.

# to connect a post to an actual group
from subgroups.models import SubGroup

# connect post to current user
from django.contrib.auth import get_user_model
User = get_user_model()

class Reply(models.Model):
	user = models.ForeignKey(User, related_name='replies',on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now=True)
	message = models.TextField()
	subgroup = models.ForeignKey(SubGroup, related_name='replies_relatedname', null=True, blank=True,on_delete=models.CASCADE)
	last_clicked_pk = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return self.message

	# def save(self, *args, **kwargs):
	# 	self.message_html = misake.html(self.message)
	# 	super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse("subgroups:replies", kwargs={'pk':self.subgroup.pk})

	
											
	class Meta:
		ordering = ['-created_at']

