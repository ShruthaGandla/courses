from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [ url(r'^$', views.index),
                url(r'^create$', views.createCourse),
                url(r'^delete/(?P<id>\d+)$', views.removeCourse),
                url(r'^okaydestroy/(?P<id>\d+)$', views.destroyCourse)]
