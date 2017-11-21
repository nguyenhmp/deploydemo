from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^new$', views.new),
    url(r'^$', views.index),
    url(r'^(?P<user_id>\d+)$', views.update),
    url(r'^(?P<user_id>\d+)/edit$', views.edit),


]