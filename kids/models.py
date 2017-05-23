from django.db import models
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField



class SliderKids(models.Model):
    link = models.CharField('Ссылка', max_length=255)
    title = models.CharField('Подпись картинки', max_length=255)
    image = models.ImageField(upload_to='media/static/upload/slider-kids/', blank=True, verbose_name='Файл')
    def image_tag(self):
        return mark_safe('<img src="/media/%s" style="max-width:300px;"/>' % (self.image))

    image_tag.short_description = 'Предпросмотр'

    class Meta:
         verbose_name_plural = "Слайдер детское отделение"




class Programs(models.Model):
    title =  models.CharField('Название программы', max_length=255)
    response =  RichTextUploadingField('Содержание')
    class Meta:
         verbose_name_plural = "Программы"




class PhotoKids(models.Model):
    CITY_CHOICES = (
        ('1', 'Екатеринбург'),
        ('2', 'Курган'),
        ('3', 'Магнитогорск'),
        ('4', 'Челябинск'),
    )
    sortir = models.IntegerField('Сортировка', blank=True, default=0)
    city = models.CharField('Филиал',choices=CITY_CHOICES,max_length=255)
    small_image = models.ImageField(upload_to='static/upload/Photos/kids/small/', verbose_name='Превью')
    big_image = models.ImageField(upload_to='static/upload/Photos/kids/big/', verbose_name='Оригинал')
    title = models.CharField('Подпись картинки', max_length=255, blank=True)

    def image_small_p(self):
        return mark_safe('<img src="/media/%s" style="max-width:100px;"/>' % (self.small_image))
    image_small_p.short_description = 'Предпросмотр'

    def big_image_p(self):
        return mark_safe('<img src="/media/%s" style="max-width:100px;"/>' % (self.big_image))
    big_image_p.short_description = 'Предпросмотр'

    class Meta:
         verbose_name_plural = "Фотографии"












class Doctors(models.Model):
    CITY_CHOICES = (
        ('1', 'Екатеринбург'),
        ('2', 'Курган'),
        ('3', 'Магнитогорск'),
        ('4', 'Челябинск'),
    )
    name = models.CharField('Имя', max_length=255)
    work = models.CharField('Специальность', max_length=255)
    email = models.CharField('Почта', max_length=255 , blank=True)
    city = models.CharField('Город',choices=CITY_CHOICES,max_length=255)
    sortdoc = models.IntegerField('Сортировка', blank=True)
    text  = RichTextUploadingField('Информация о докторе')
    image1 = models.ImageField(upload_to='static/upload/Doctors/270/', verbose_name='Картинка 270 Х 270')
    image2 = models.ImageField(upload_to='static/upload/Doctors/360/', verbose_name='Картинка 270 Х 360')
    image3 = models.ImageField(upload_to='static/upload/Doctors/520/', verbose_name='Картинка 520 Х 660')
    image4 = models.ImageField(upload_to='static/upload/Doctors/520/', blank=True, verbose_name='Дополнительная картинка 520 Х 660')

    def image_tag1(self):
        return mark_safe('<img src="/media/%s" style="max-width:100px;"/>' % (self.image1))
    image_tag1.short_description = 'Предпросмотр'

    def image_tag2(self):
        return mark_safe('<img src="/media/%s" style="max-width:100px;"/>' % (self.image2))
    image_tag2.short_description = 'Предпросмотр'

    def image_tag3(self):
        return mark_safe('<img src="/media/%s" style="max-width:100px;"/>' % (self.image3))
    image_tag3.short_description = 'Предпросмотр'

    def image_tag4(self):
        return mark_safe('<img src="/media/%s" style="max-width:100px;"/>' % (self.image4))
    image_tag4.short_description = 'Предпросмотр'

    def __str__(self):              # __unicode__ on Python 2
        return self.name

    class Meta:
         verbose_name_plural = "Наши специалисты детское"

    #######################################################




class TestimonialsKids(models.Model):
    name = models.CharField('Имя', max_length=255)
    date = models.DateField('Дата')
    doc = models.ManyToManyField(Doctors, verbose_name='Доктор', blank=True)
    text  = RichTextUploadingField('Отзыв')
    switch = models.BooleanField('Опубликовать')
    class Meta:
         verbose_name_plural = "Отзывы"
