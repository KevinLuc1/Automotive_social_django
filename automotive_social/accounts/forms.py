# returns user model currently active
from django.contrib.auth import get_user_model
# Usercreationform is already built in to the auth package
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):

	class Meta:
		fields = ('username', 'email', 'password1', 'password2')
		model = get_user_model()

	# customeize the labels on the form
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.fields["username"].label = "Display name"
		self.fields["email"].label = "Email address"

