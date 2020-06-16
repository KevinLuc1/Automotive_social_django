from django.shortcuts import render
from django.views import generic
from groups.models import Group
# from . import models


class ListGroups(generic.ListView):
	# automatically looks for a group_list.html
	model = Group

# # displays all the subgroups based on group clicked
# class SingleGroup(generic.DetailView):
# 	# auto looks for group_detail.html
# 	model = Group

	# context_object_name = 'single_group_detail'



	# def get_context_data(self, **kwargs):
		
	# 	context = super().get_context_data(**kwargs)
	# 	context['single_group_detail'] = Group.objects.all()

	# 	return context