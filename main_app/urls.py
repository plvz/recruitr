from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^positions/$', views.positions),
    url(r'^post_position/$', views.post_position),


]
