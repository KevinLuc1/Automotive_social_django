from django.urls import path, include
from groups.views import ListGroups

app_name = "groups"

urlpatterns = [
	path('', ListGroups.as_view(), name='all'),
	# path('posts/', include("posts.urls", namespace="posts")),
    # path('subgroups/',include("subgroups.urls", namespace="subgroups")),

    # example 127.0.0.1:8000/audi
    # path('<slug>/', SingleGroup.as_view(), name='single'),


	# path("subgroups/in/<slug>/",views.SingleSubGroup.as_view(),name="single"),

]