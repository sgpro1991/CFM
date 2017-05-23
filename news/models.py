from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe
# Create your models here.





class News(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    image = models.ImageField(upload_to='static/upload/news/', blank=True, verbose_name='Картинка')
    description = models.CharField('Описание', max_length=255)
    date = models.DateTimeField('Дата время')
    text  = RichTextUploadingField('Текст')
    confirm = models.BooleanField('Опубликовать',blank=True,default=False)
    def image_tag(self):
        return mark_safe('<img src="/media/%s" style="max-width:300px;"/>' % (self.image))
    image_tag.short_description = 'Предпросмотр'

    class Meta:
         verbose_name_plural = "Новости"





class Stock(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    image = models.ImageField(upload_to='static/upload/news/', blank=True, verbose_name='Картинка')
    description = models.CharField('Описание', max_length=255)
    date = models.DateTimeField('Дата время')
    text  = RichTextUploadingField('Текст')

    def image_tag(self):
        return mark_safe('<img src="/media/%s" style="max-width:300px;"/>' % (self.image))
    image_tag.short_description = 'Предпросмотр'

    class Meta:
         verbose_name_plural = "Акции"







class NewsKids(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    image = models.ImageField(upload_to='static/upload/news/', blank=True, verbose_name='Картинка')
    description = models.CharField('Описание', max_length=255)
    date = models.DateTimeField('Дата время')
    text  = RichTextUploadingField('Текст')

    def image_tag(self):
        return mark_safe('<img src="/media/%s" style="max-width:300px;"/>' % (self.image))
    image_tag.short_description = 'Предпросмотр'

    class Meta:
         verbose_name_plural = "Новости детское"
