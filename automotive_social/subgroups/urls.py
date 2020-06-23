from django.urls import path
from . import views

app_name = 'subgroups'

urlpatterns = [
	path('<slug>', views.ListSubGroups.as_view(), name='all'),
	path('create/', views.CreateSubGroup.as_view(), name='create'),
	path("<pk>/", views.ListSingleSubGroup.as_view(),name="replies"),
]