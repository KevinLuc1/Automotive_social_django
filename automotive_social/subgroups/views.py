from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.urls import reverse
from django.views import generic
from django.shortcuts import get_object_or_404

from subgroups.models import SubGroup

from replies.models import Reply


from . import models

from django.contrib.auth import get_user_model
User = get_user_model()




# Create your views here.

# anyone logged in can create a subgroup
class CreateSubGroup(LoginRequiredMixin, generic.CreateView):
	# allowable fields to enter from SubGroup model
	fields = ('name', 'description', 'group')
	model = SubGroup

	# check if form is valid
	# This method is called when valid form data has been POSTed.
	def form_valid(self, form):
		# soft save, dont send to database yet
		self.object = form.save(commit=False)
		# we need to connect this new post to the actual user itself at the request
		self.object.user = self.request.user

		print("hello {}".format(self.request))
		# self.object.group = self.request

		# hard save, send to database
		self.object.save()
		return super().form_valid(form)




# auto looks for subgroup_list.html
class ListSubGroups(generic.ListView):

	model = SubGroup
	
	def get_context_data(self, **kwargs):
		
		context = super().get_context_data(**kwargs)


		# hello = SubGroup.objects.filter(group__slug=self.kwargs['slug'])
		# hello2 = hello.0.group.slug

		# query through all subgroups, look for foreign keys where the slug is equal to slug of input
		# ie: click on 'audi', will look for subgroups tied with 'audi' foregin key
		context['related_subgroups'] = SubGroup.objects.filter(group__slug=self.kwargs['slug'])

		# context['hello'] = hello2

		return context


# auto looks for subgroup_detail.html
# shows details about the subgroup, like posts inside the subgroup
class ListSingleSubGroup(generic.DetailView):
	model = SubGroup


	# def get_queryset(self):
	# 	queryset = super().get_queryset()




	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		# save the pk of most recent subgroup clicked. pull this when creating reply
		# rigging to use last_name inside User model instead of creating new field

		current_user = self.request.user

		save_pk_of_subgroup_clicked = User.objects.get(username=current_user)

		save_pk_of_subgroup_clicked.last_name = self.object.pk

		save_pk_of_subgroup_clicked.save()

		return context







