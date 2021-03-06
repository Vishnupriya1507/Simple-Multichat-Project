"""multichat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import include,url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from chat.views import index


urlpatterns = [
    url(r'^$', index, name='homepage'),  # The start point for index view
    url(r'^chat/', include('chat.urls')),
    url(r'^accounts/login/$',login, name='login'),  # The base django login view
    url(r'^chat/logout/$', logout, name='logout'),  # The base django logout view
    url(r'^admin/', admin.site.urls),  # etc :D
    #url(r'^accounts/',include('allauth.urls')),   
    #url(r'^accounts/login/chat/logout/$', logout, name='logout'),
]