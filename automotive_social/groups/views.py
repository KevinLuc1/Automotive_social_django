from django.shortcuts import render
from django.views import generic
from groups.models import Group
# from . import models


class ListGroups(generic.ListView):
	# automatically looks for a group_list.html
	model = Group

