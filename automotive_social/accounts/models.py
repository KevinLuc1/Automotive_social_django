from django.db import models

from django.contrib import auth

# inherit from built in django 'auth' and 'models'
# we're using django's built in .User to create a class User
class User(auth.models.User, auth.models.PermissionsMixin):
	# we'll normally name attributes here but by using the django buult in user
	# we already have username email password1 password2 already set up here

	# last_clicked_subgroup_name = models.CharField(max_length=30, blank=True)

	def __str__(self):
		# .username is a built in attribute that comes with .User
		return "@{}".format(self.username)


class Last_location(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	last_pk = models.CharField(max_length=255, blank=True)