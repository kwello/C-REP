"""crime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include, re_path
from test import views

#urlpatterns = [
#    path('admin/', admin.site.urls),
#   path('', include('polls.urls')),
#]

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^$', views.homepage),
    re_path('^register/$', views.register),
    re_path('^signin/$', views.signin),
    re_path('^dosignup/$', views.dosignup),
    re_path('^dosignin/$', views.dosignin),
    re_path('^logout/$', views.logout),
]
