from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
#    url(r'^$', views.about, name='about'),
    url(r'^about/$', views.about, name='about'),
    url(r'^home/$', views.home, name='home'),
    url(r'^help/$', views.help, name='help'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^restricted/', views.restricted, name='restricted'),
]
