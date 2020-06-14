from django.shortcuts import render
from django.views.generic.list import ListView
from groups.models import Group
# from . import models


class ListGroups(ListView):
	# automatically looks for a group_list.html
	model = Group
	# context_object_name = 'object_list'

	# def get_context_data(self, **kwargs):
	# 	context = super().get_context_data(**kwargs)
	# 	context['group_names'] = Group.objects.all()
	# 	return context
		

	# def get_queryset(self):
	# 	return Group.objects.filter()order_by('name')