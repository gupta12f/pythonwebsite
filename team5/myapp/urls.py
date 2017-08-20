from django.conf.urls import url
from . import views
from myapp.views import Index,Detail
urlpatterns = [
        url(r'^$', Index.as_view(), name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^(?P<course_no>\d{3,3})/$', Detail.as_view(), name='detail'),
        url(r'^addtopic/$', views.addtopic, name='addtopic'),
        url(r'^topics/$', views.topics, name='topics'),
        url(r'^topicdetails/(?P<topic_id>\d*)/$',views.topicdetail, name='topicdetails'),
        url(r'^register/$',views.register,name='register'),
        url(r'^login/$',views.user_login, name='login'),
        url(r'^mycourses/$',views.mycourses, name='mycourses'),
        url(r'^logout/$',views.user_logout, name='logout')
        ]
