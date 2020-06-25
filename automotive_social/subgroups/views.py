from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.urls import reverse
from django.views import generic
from django.shortcuts import get_object_or_404

from subgroups.models import SubGroup
from groups.models import Group
from replies.models import Reply


from . import models

from django.contrib.auth import get_user_model
User = get_user_model()




# Create your views here.

# anyone logged in can create a subgroup
class CreateSubGroup(LoginRequiredMixin, generic.CreateView):
	# allowable fields to enter from SubGroup model
	fields = ('name', 'description')
	model = SubGroup

	# check if form is valid
	# This method is called when valid form data has been POSTed.
	def form_valid(self, form):
		# soft save, dont send to database yet
		self.object = form.save(commit=False)
		# we have a required username field
		# we need to connect this new post to the actual user itself at the request
		self.object.user = self.request.user
		# the primary key of the most recent group clicked was saved to the user's "first_name" field
		# save the pk we saved
		mypk = self.request.user.first_name
		# look for the name of the Group based off the primary key we saved
		name_of_group = Group.objects.get(pk=mypk)
		# we have a required group field
		# assign the name of group to the group field inside the form
		self.object.group = name_of_group
		# hard save the form to send info to the database
		self.object.save()
		return super().form_valid(form)




# auto looks for subgroup_list.html
class ListSubGroups(generic.ListView):

	model = SubGroup
	
	def get_context_data(self, **kwargs):
		
		context = super().get_context_data(**kwargs)

		# query through all subgroups, look for foreign keys where the slug is equal to slug of input
		# ie: click on 'audi', will look for subgroups tied with 'audi' foregin key
		# context related_subgroups will be used inside the url template of the subgroup_list.html page
		context['related_subgroups'] = SubGroup.objects.filter(group__slug=self.kwargs['slug'])




		if self.request.user.is_authenticated:
			'''
			Once the user clicks on a item in ListView, I want to save the primary key of that Group
			We'll later use that pk to fill in the group field when creating a new subgroup/ new post
			'''

			# save the request.path of the url
			# returns:  /subgroups/audi
			path_name = self.request.path

			# split the path name at the '/'
			# returns:  ['', 'subgroups', 'audi']
			path_name_split = path_name.split('/')

			# save the slug name used in the url path
			# returns:  audi 
			slug_from_url = path_name_split[-1]

			# filter through Group objects and look for the group where slug is equal to slug from url
			data_from_group = Group.objects.filter(slug=slug_from_url)

			# grab the primary key of the Group based off the slug input
			pk_to_send_to_user_model = data_from_group.get().pk

			# this is the current active user logged in
			current_user = self.request.user

			# Grab the username inside User model based on the current active logged in user
			mypk = User.objects.get(username=current_user)

			# overwrite the default first_name field with the primary key of group that was clicked on
			mypk.first_name = pk_to_send_to_user_model

			# send to database the pk, we'll later use this pk to for creating new subgroups/creating new posts
			mypk.save()

		return context


# auto looks for subgroup_detail.html
# shows details about the subgroup, like posts inside the subgroup
class ListSingleSubGroup(generic.DetailView):
	model = SubGroup



	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)


		if self.request.user.is_authenticated:

			# save the pk of most recent subgroup clicked. pull this when creating reply
			# rigging to use last_name inside User model instead of creating new field

			current_user = self.request.user

			save_pk_of_subgroup_clicked = User.objects.get(username=current_user)

			save_pk_of_subgroup_clicked.last_name = self.object.pk

			print("this is self.object inside views py subgroups: {}".format(self.object))
			# print("this is self.object.group inside views py subgroups: {}".format(self.object.group))

			save_pk_of_subgroup_clicked.save()

		return context







