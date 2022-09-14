"""just URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from git import views


urlpatterns = [
    path("",views.index,name= 'home'),

    path("gitplayer",views.gitplayer,name= 'gitplayer'),
    path("about",views.about,name= 'about'),
    path("contactus",views.contactus,name= 'contactus'),
    path("CQM",views.CQM,name= 'CQM'),
    path("MFPW",views.MFPW,name= 'MFPW'),
    path("LA",views.LA,name= 'LA'),
    path("EANDI",views.EANDI,name= 'EANDI'),
    path("PLC",views.PLC,name= 'PLC'),
    path("STPM",views.STPM,name= 'STPM'),
    path("contactus#",views.index,name= 'home'),
    path("about#",views.index,name= 'home')

         
]
