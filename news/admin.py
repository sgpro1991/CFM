from django.contrib import admin

# Register your models here.
from .models import *

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','date','confirm']
    #readonly_fields = ('date_time',)
    search_fields = ['title']
    #fields = ('title' ,'description','date','image','image_tag', 'text')
    readonly_fields = ('image_tag',)
    list_editable = ('confirm',)



class NewsKidsAdmin(admin.ModelAdmin):
    list_display = ['title','date']
    #readonly_fields = ('date_time',)
    fields = ('title' ,'description','date','image','image_tag', 'text')
    readonly_fields = ('image_tag',)



class StockAdmin(admin.ModelAdmin):
    list_display = ['title','date']
    #readonly_fields = ('date_time',)
    fields = ('title' ,'description','date','image','image_tag', 'text')
    readonly_fields = ('image_tag',)



admin.site.register(Stock,StockAdmin)

admin.site.register(NewsKids,NewsKidsAdmin)
admin.site.register(News,NewsAdmin)
