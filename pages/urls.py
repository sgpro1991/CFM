
from django.conf.urls import url,include
from pages.views import *



urlpatterns = [
    url(r'^$', Main),

    #url(r'^landing/', Landing),

    url(r'^doctors+\.html/', Docktors),
    url(r'^questions+\.html/', Questions),
    url(r'^form/testimonials/', FormTestimonials),

    url(r'^form/testimonials-kids/', FormTestimonialsKids),


    url(r'^form/online/', FormOnline),
    url(r'^form/communication/', FormCommunicate),
    url(r'^form/faq/', FormFaq),


    url(r'^stock/(?P<sid>\d+)/$', GetStockF),

    url(r'^comment/(?P<sid>\d+)/$', CommentDoc),



    url(r'^stock/$', StockF),

    url(r'^send_email/', SendEmail),
    url(r'^form/send-email-doc/', SendEmailForm),


    url(r'^testimonials/',TestimonialsUsers),
    url(r'^page/', include('django.contrib.flatpages.urls')),
    url(r'^about_tes/',AboutTes),
    url(r'^about_tes_kids/',AboutTesKids),


    url(r'^photo+\.html/', PhotosMain),
    url(r'^last_news/', LastNews),

    url(r'^anketa/', AnketaF),

    url(r'^about_news_all/', AboutNewsAll),

    url(r'^form/psyhology/', FormAnketa),



]
