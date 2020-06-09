from django.db import models

from django.contrib import auth

# inherit from built in django 'auth' and 'models'
# we're using django's built in .User to create a class User
class User(auth.models.User, auth.models.PermissionsMixin):
	# we'll normally name attributes here but by using the django buult in user
	# we already have username email password1 password2 already set up here

	def __str__(self):
		# .username is a built in attribute that comes with .User
		return "@{}".format(self.username)


