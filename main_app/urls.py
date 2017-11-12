from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from . import views

urlpatterns = [
    url(r'^$', views.positions,name='index'),
    url(r'^([0-9]+)/$', views.detail_position,name='edit position'),
    url(r'^post_position/$', views.post_position, name='post position'),
    url(r'^([0-9]+)/post_applicant/$', views.post_applicant, name='post applicant'),
    url(r'^([0-9]+)/applicant/([0-9]+)/$', views.detail_applicant,name='detail applicant'),
    url(r'^employee/$', views.employee,name='add employee'),
    url(r'^post_employee/$', views.post_employee,name='post employee'),
    url(r'^post_event/$', views.post_event,name='post event'),



]
