"""
URL configuration for blogs project.

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
from django.urls import path
from django.urls import include, re_path
# from django.conf.urls import url
from boards import views
urlpatterns = [
    path('', views.home, name='home'),
    # re_path(r'^$', views.home, name='home'),
    re_path(r'^questions/(?P<pk>\d+)/$', views.question, name='question'),
    re_path(r'^posts/(?P<slug>[-\w]+)/$', views.post, name='post'),
    re_path(r'^blog/(?P<slug>[-\w]+)-(?P<pk>\d+)/$', views.blog_post, name='blog_post'),
    re_path(r'^profile/(?P<username>[\w.@+-]+)/$', views.user_profile, name='user_profile'),
    re_path(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive, name='year'),

    re_path(r'^about/$', views.about, name='about'),
    re_path(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    path('admin/', admin.site.urls),
]
