from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *
from news.models import NewsKids



def MainKids(request):
    images = SliderKids.objects.all()
    return render(request,'kids_main.html', {'pic':images})


def ProgramsView(request):
    programs = Programs.objects.all()
    return render(request,'programs.html', {'programs':programs})



def DocktorsKids(request):
    return HttpResponse(1)



def PhotoKidsF(request):
    photo = PhotoKids.objects.all().order_by('sortir')
    chose = PhotoKids.CITY_CHOICES
    mass = []
    for a in chose:
        mass.append({'id':a[0],'city':a[1]})
    return render(request,'photo-kids.html',{'photo':photo,'city':mass})



#################
# ДОкторы
#################
def DocktorsKids(request):
    doc = Doctors.objects.all().order_by('sortdoc')
    chose = Doctors.CITY_CHOICES
    mass = []
    for a in chose:
        mass.append({'id':a[0],'city':a[1]})
    return render(request,'docktors-kids.html',{'doc':doc,'city':mass})




def NewsKidsF(request):
    item = request.GET.get('id',False)

    if item:
        news = NewsKids.objects.get(id=item)
        return render(request,'news-kids-item.html',{'news':news})

    else:
        news = NewsKids.objects.filter().order_by('-date')[0:10]
        return render(request,'news-kids.html',{'news':news})




def TestimonialsKidsF(request):
    otz = TestimonialsKids.objects.filter(switch = True).order_by('-date')[0:5]
    return render(request,'testimonials-kids.html', {'otz':otz})
