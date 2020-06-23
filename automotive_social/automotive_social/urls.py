"""automotive_social URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.HomePage.as_view(), name='home'),
    path('accounts/', include("accounts.urls", namespace="accounts")),
    path('accounts/', include("django.contrib.auth.urls")),
    path('login_msg/', views.LoggedInPage.as_view(), name="login_msg"),
    path('logout_msg/', views.LoggedOutPage.as_view(), name="logout_msg"),
    path('', include("groups.urls", namespace="groups")),
    path('subgroups/', include("subgroups.urls", namespace="subgroups")),
    path('replies/', include("replies.urls", namespace="replies")),

]
