from django.conf.urls import url
from . import views
app_name='cleub'

urlpatterns = [
    
    url(r'^$', views.index, name='index'),
    url(r'about/$', views.about, name='about'),
    url(r'^services/$', views.services, name='services'),
    url(r'^thanks/$', views.thanks, name='thanks'),
    url(r'^product/$', views.product, name='product'),
    url(r'^contactus/$', views.contactus, name='contactus'),

    
]