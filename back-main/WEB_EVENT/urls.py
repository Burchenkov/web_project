"""
URL configuration for WEB_EVENT project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include, re_path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    re_path('^signup/$', views.UserCreateView.as_view(), name='sign_up'),
    re_path('^signin/$', views.user_login),
    re_path('^events/$', views.events_get),
    re_path('^event_add/$', views.event_add),
    re_path('^event_change/(?P<pk>[0-9]+)$', views.event_change),
]
