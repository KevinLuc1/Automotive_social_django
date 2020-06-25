from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse
from django.views import generic
from django.shortcuts import get_object_or_404

from replies.models import Reply

from subgroups.models import SubGroup

from . import models

# Create your views here.

# anyone logged in can create a reply
class CreateReply(LoginRequiredMixin, generic.CreateView):
	# allowable fields to enter from Reply model
	fields = ('message',)
	model = Reply

	# check if form is valid
	# This method is called when valid form data has been POSTed.
	def form_valid(self, form):
		# soft save without sending to database, make changes before saving
		self.object = form.save(commit=False)
		# grab to current active user(request), save that to the user field in form
		self.object.user = self.request.user

		# set mypk to the pk saved under 'last_name'
		mypk = self.request.user.last_name

		# find the name of the subgroup based on saved mypk
		doot = SubGroup.objects.get(pk=mypk)	

		# assign saved subgroup to the subgroup field in form
		self.object.subgroup = doot

		# hard save, send to database
		self.object.save()
		return super().form_valid(form)




