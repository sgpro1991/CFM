from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import News



def Main(request):
    description_seo = 'Новости Центра Семейной Медицины. Следите за обновлениями.'
    try:
        if request.COOKIES['sessionid']:
            news = News.objects.filter().order_by('-date')[0:6]
            return render(request,'news.html',{'news':news,'title_seo':'- Новости','description_seo':description_seo})

    except:
            news = News.objects.filter(confirm=True).order_by('-date')[0:6]
            return render(request,'news.html',{'news':news,'title_seo':'- Новости','description_seo':description_seo})



def GetNews(request,nid):
    news = News.objects.get(id=nid)
    return render(request,'news-item.html',{'news':news})
