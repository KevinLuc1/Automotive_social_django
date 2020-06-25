from django.shortcuts import render
from django.views import generic
from groups.models import Group
# from . import models

from django.contrib.auth import get_user_model
User = get_user_model()




class ListGroups(generic.ListView):
	# automatically looks for a group_list.html
	model = Group

	

	# def get_context_data(self, **kwargs):
	# 	context = super().get_context_data(**kwargs)

	# # 	# save the pk of most recent subgroup clicked. pull this when creating reply
	# # 	# rigging to use first_name inside User model instead of creating new field


	# 	print('this is self.request.user {}'.format(self.request.user))

	# 	print('this is self.object {}'.format(self))

	# 	# hello = Group.objects.all()
	# 	# print(hello)





	# # 	# current_user = self.request.user

	# # 	# save_pk_of_subgroup_clicked = User.objects.get(username=current_user)

	# # 	# save_pk_of_subgroup_clicked.first_name = self.object.pk

	# # 	# save_pk_of_subgroup_clicked.save()

	# 	return context



