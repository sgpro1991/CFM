from django.conf.urls import url,include
from kids.views import *


urlpatterns = [
    url(r'^$', MainKids),
    url(r'^programs+\.html/', ProgramsView),
    url(r'^kids-photo+\.html/', PhotoKidsF),
    url(r'^page/', include('django.contrib.flatpages.urls')),
    url(r'^special/', DocktorsKids),
    url(r'^kids-news/', NewsKidsF),
    url(r'^testimonials/', TestimonialsKidsF),



]
