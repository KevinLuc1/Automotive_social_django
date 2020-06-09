# returns user model currently active
from django.contrib.auth import get_user_model
# Usercreationform is already built in to the auth package
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):

	class Meta:
		# we can choose more fields if needed, password1 is create password, password2 is confirm password
		fields = ('username', 'email', 'password1', 'password2')
		model = get_user_model()

	# optional customize the labels on the form
	def __init__(self,*args,**kwargs):
		self.fields["username"].label = "Display name"
		super().__init__(*args,**kwargs)
		self.fields["email"].label = "Email address"

