from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse
from django.views import generic
from django.shortcuts import get_object_or_404

from replies.models import Reply
# from groups.models import Group

from . import models

# Create your views here.

# anyone logged in can create a reply
class CreateReply(generic.CreateView):
	# allowable fields to enter from Reply model
	fields = ('message', 'subgroup')
	model = Reply

	# check if form is valid
	# This method is called when valid form data has been POSTed.
	def form_valid(self, form):
		# soft save, dont send to database yet
		self.object = form.save(commit=False)
		# we need to connect this new post to the current active user at the request
		self.object.user = self.request.user

		print("hello {}".format(self.object.pk))

		# self.object.subgroup = self.request

		# hard save, send to database
		self.object.save()
		return super().form_valid(form)



