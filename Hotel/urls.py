from django.conf.urls import url
from .views import *

urlpatterns =[
    url(r'^$', index, None, 'index'),
    url(r'^about/', about, None, 'about'),
    url(r'^roominfo/', roomInfo, None, 'roomInfo'),
    url(r'^order/', order, None, 'order'),
    url(r'^orderresult/', orderResult, None, 'orderResult')
]