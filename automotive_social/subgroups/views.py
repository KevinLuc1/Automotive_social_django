from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.urls import reverse
from django.views import generic
from django.shortcuts import get_object_or_404

from subgroups.models import SubGroup
# from groups.models import Group

from . import models

# Create your views here.

# anyone logged in can create a subgroup
class CreateSubGroup(LoginRequiredMixin, generic.CreateView):
	# allowable fields to enter from SubGroup model
	fields = ('name', 'description')
	model = SubGroup

# auto looks for subgroup_list.html
class ListSubGroups(generic.ListView):
	model = SubGroup

	
	
	def get_context_data(self, **kwargs):
		
		context = super().get_context_data(**kwargs)

		context['hello'] = self.kwargs['slug']

		monkey = self.kwargs['slug']

		context['hello2'] = SubGroup.objects.filter(group__slug=self.kwargs['slug'])

		


		return context


# auto looks for subgroup_detail.html
# shows details about the subgroup, like posts inside the subgroup
class ListSingleSubGroup(generic.DetailView):
	model = SubGroup






