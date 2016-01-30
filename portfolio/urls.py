from django.conf.urls import url
from portfolio import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add, name='add'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
   
]