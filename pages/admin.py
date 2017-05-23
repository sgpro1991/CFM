from django.contrib import admin
from django.forms import CheckboxSelectMultiple
# Register your models here.


from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.db import models

from ckeditor.widgets import CKEditorWidget


from .models import *





class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ['name','date','switch']
    search_fields = ['name']
    list_editable = ['switch']
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }






class FlatPageCustom(FlatPageAdmin):

    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }
    fieldsets = (
        (None, {'fields': ('url','title_seo','keywords_seo','description_seo', 'title', 'content','phone', 'sites','template_name')}),
        #(None, {'fields': ('url', 'title', 'content1_header', 'content', 'content2_header', 'content2', 'template_name', 'sites')}),
    )

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageCustom)





class FaqAdmin(admin.ModelAdmin):
    list_display = ['question']



class SliderAdmin(admin.ModelAdmin):
    list_display = ['title','sortir', 'link','image_tag']
    fields = ('sortir','title' ,'link','image', 'image_tag',)
    readonly_fields = ('image_tag',)
    list_editable = ('sortir',)




class DoctorsAdmin(admin.ModelAdmin):
    list_display = ['name', 'image_tag1','sortdoc']
    search_fields = ['name']
    list_filter = ['city']
    readonly_fields = ('image_tag1','image_tag2','image_tag3','image_tag4',)
    list_editable = ('sortdoc',)



class MessagesAdmin(admin.ModelAdmin):
    list_display = ['name','datetime','type_message']
    search_fields = ['name']
    list_filter = ['type_message']



class RecordOnlineAdmin(admin.ModelAdmin):
    list_display = ['name','datetime','phone','datetime_record','doc','control','itog']
    search_fields = ['name']
    list_filter = ['control','itog','datetime_record']
    list_editable = ('control','datetime_record','doc','itog')





class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id','title','sortir', 'city', 'image_small_p']
    search_fields = ['title']
    list_filter = ['city']
    list_editable = ('title','sortir',)
    readonly_fields = ('image_small_p',)



class PhotoKidsAdmin(admin.ModelAdmin):
    list_display = ['title', 'city', 'image_small_p']
    search_fields = ['title']
    list_filter = ['city']
    readonly_fields = ('image_small_p',)



class CountersAdmin(admin.ModelAdmin):
    list_display = ['id','mon', 'vrt', 'kids','filials','doctors']
    list_editable = ('mon','vrt','kids','filials','doctors')


admin.site.register(Counters,CountersAdmin)
admin.site.register(RecordOnline,RecordOnlineAdmin)
admin.site.register(Testimonials,TestimonialsAdmin)
admin.site.register(Faq,FaqAdmin)
admin.site.register(Slider,SliderAdmin)
admin.site.register(Doctors,DoctorsAdmin)
admin.site.register(Messages,MessagesAdmin)
admin.site.register(Photo,PhotoAdmin)
