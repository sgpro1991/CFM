from django.conf.urls import url,include
from news.views import *


urlpatterns = [
    url(r'^$', Main),
    url(r'(?P<nid>\d+)/$', GetNews),
]
