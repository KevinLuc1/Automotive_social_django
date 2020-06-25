from django.urls import path
from . import views

app_name = 'replies'

urlpatterns = [
	path('create/', views.CreateReply.as_view(), name='create'),
	
]