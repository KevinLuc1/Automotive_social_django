from django.urls import path
from groups.views import ListGroups

app_name = "groups"

urlpatterns = [
	path('', ListGroups.as_view(), name='all')

]