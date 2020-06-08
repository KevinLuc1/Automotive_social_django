from django.db import models

from django.contrib import auth

# inherit from built in django 'auth' and 'models'
# we're using django's built in .User to create a class User
class User(auth.models.User, auth.models.PermissionsMixin):

	def __str__(self):
		# .username is a built in attribute that comes with .User
		return "@{}".format(self.username)


