from django.contrib import admin

# Register your models here.
from .models import *
from django.forms import CheckboxSelectMultiple


class TestimonialsKidsAdmin(admin.ModelAdmin):
    list_display = ['name','date','switch']
    search_fields = ['name']
    list_editable = ['switch']
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }



class SliderKidsAdmin(admin.ModelAdmin):
    list_display = ['title', 'link','image_tag']
    fields = ('title' ,'link','image', 'image_tag',)
    readonly_fields = ('image_tag',)


class ProgramsAdmin(admin.ModelAdmin):
    list_display = ['title']





class DoctorsAdmin(admin.ModelAdmin):
    list_display = ['name', 'image_tag1','sortdoc']
    search_fields = ['name']
    list_filter = ['city']
    readonly_fields = ('image_tag1','image_tag2','image_tag3','image_tag4',)
    list_editable = ('sortdoc',)






class PhotoKidsAdmin(admin.ModelAdmin):
    list_display = ['id','title','sortir', 'city', 'image_small_p']
    search_fields = ['title']
    list_filter = ['city']
    list_editable = ('title','sortir',)
    readonly_fields = ('image_small_p',)




admin.site.register(TestimonialsKids,TestimonialsKidsAdmin)
admin.site.register(SliderKids,SliderKidsAdmin)
admin.site.register(Programs,ProgramsAdmin)
admin.site.register(Doctors,DoctorsAdmin)
admin.site.register(PhotoKids,PhotoKidsAdmin)
