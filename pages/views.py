from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from django.shortcuts import redirect
from .models import *
from django.template.defaultfilters import date as _date
from datetime import datetime
import json
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

from kids.models import TestimonialsKids

from news.models import *
import requests

from .template_mail import TmpMail



def Landing(request):
    return render(request,'landing.html')


def views404(request):
     return redirect('/')


def Main(request):

    title_seo = '- Гинекология. Репродуктивный центр. Урологический центр. ЭКО.'
    keywords_seo = 'ЦСМ, Гистероскопия екатеринбург, бесплодие екатеринбург, Гистероскопия, екатеринбург, Миома матки, Полип эндометрия,  Гиперплазия эндометрия, Патология матки, Эндометриоз, Непроходимость маточных труб, Бесплодие, Лечение бесплодия, Мужское бесплодие, Эко, Эко по омс, Спермограмма, Спермограмма екатеринбург, Анализ спермограммы, Где сдать спермограмму,  Гистероскопия, Лапароскопия, внутриматочная инсеминация, ведение беременности, консультация гинеколога, эко по омс, криоконсервация спермы, криоконсервация яйцеклеток, гормональные исследования, клиника эко, гинекологические операции, гинекологические операции екатеринбург'
    description_seo = 'Центр семейной медицины создан в Екатеринбурге в январе 2001 года. Актуальность появления специализированной клиники по лечению бесплодия методами вспомогательных репродуктивных технологий (ВРТ) была обусловлена высоким процентом бесплодных супружеских пар в Уральском регионе и общей мировой тенденцией развития методов лечения бесплодия человека. За годы существования клиники благодаря работе персонала на свет появились более тысячи младенцев, зачатых «в пробирке»'
    images = Slider.objects.all().order_by('sortir')
    counters = Counters.objects.get(id=1)
    return render(request,'index.html', {'pic':images,'title_seo':title_seo,'keywords_seo':keywords_seo,'description_seo':description_seo,'count':counters})




'''
from datetime import datetime
import locale

def GetTestimonials(request):
    r = requests.get('http://www.cfm.ru/manager/systemctl/')
    data = r.json()
    d = {'января': 'январь', 'декабря': 'декабрь','апреля':'апрель','мая':'май','июня':'июнь','июля':'июль','августа':'август','сентября':'сентябрь','октября':'октябрь','ноября':'ноябрь','февраля':'февраль','марта':'март'}

    for a in data:
        if a['date']:

            date_string = a['date']
            locale.setlocale(locale.LC_TIME, "ru_RU")

            for k, v in d.items():
                    date_string = date_string.replace(k, v)

            ru_date_object = datetime.strptime(date_string.strip() , '%d %B %Y').date()

            mass=[]
            doc_arr = a['doc'].split(",")



            print(mass)
            true_doc = mass
            true_date = ru_date_object #date ------------------------------------------->
            true_user = a['user'] #user ------------------------------------------------>
            true_text = a['content']

            for docs in doc_arr:
                doc = Doctors.objects.filter(name=docs).values_list('id',flat=True)
                for m in doc:
                    mass.append(m)
                #    inse = Testimonials(doc=m)
                #    inse.save()

            insert = Testimonials(name=true_user, date=true_date, text=true_text, switch=True)

            insert.save()
    return HttpResponse(0)
'''



def CommentDoc(request,sid):
    doc = Doctors.objects.get(pk=sid)
    comment = Testimonials.objects.filter(doc=sid)
    return render(request,'testimonials-doc.html',{'otz':comment, 'doc':doc})





def StockF(request):
        stock = Stock.objects.filter().order_by('-date')[0:10]
        return render(request,'stock.html',{'news':stock,'title_seo':'- Акции'})





def GetStockF(request,sid):
        stock = Stock.objects.get(id=sid)
        return render(request,'stock-tmp.html',{'stock':stock})



#################
# АНКЕТА
#################
def AnketaF(request):
    return render(request,'anketa.html')




#################
# ДОкторы
#################
def Docktors(request):
    title_seo = '- Наши специалисты'
    description_seo = 'Доктора-врачи Центра Семейной Медицины, это дружный профессиональный коллектив с огромным стажем профессиональной деятельности.'
    doc = Doctors.objects.all().order_by('sortdoc')
    chose = Doctors.CITY_CHOICES
    mass = []
    for a in chose:
        mass.append({'id':a[0],'city':a[1]})
    return render(request,'docktors.html',{'doc':doc,'city':mass,'title_seo':title_seo,'description_seo':description_seo})






def SendEmail(request):
    email = request.GET.get('docemail',False)
    if email:
        return render(request,'send-email.html',{'email':email})





#################
# Фотографии
#################
def PhotosMain(request):
    description_seo = 'Вы можете узнать как выглядит Центр Семейной Медицины изнутри ещё до посещения.'
    photo = Photo.objects.all().order_by('sortir')
    chose = Photo.CITY_CHOICES
    mass = []
    for a in chose:
        mass.append({'id':a[0],'city':a[1]})
    return render(request,'photo.html',{'photo':photo,'city':mass,'title_seo':'- Фотографии клиники. Посмотреть мед кабинеты и покои больницы.','description_seo':description_seo})












#################
# Вопросы
#################
def Questions(request):
    description_seo = 'Вопросы к специалисту по ЭКО, беременности, бесплодию, репродуктивному здоровью.'
    faq = Faq.objects.all()
    return render(request,'faq.html', {'faq':faq,'title_seo':'- Вопросы перед обращением в женскую клинику.','description_seo':description_seo})














#################
# ОТЗЫВЫ
#################
def TestimonialsUsers(request):
    description_seo = 'Узнать отзывы людей о врачах, ведение беременности, успешных эко, о клинике, о Центре Семейной Медицины.'
    otz = Testimonials.objects.filter(switch = True).order_by('-date')[0:5]
    return render(request,'testimonials.html', {'otz':otz,'title_seo':'- Отзывы о Центре Семейной Медицины на Начдива.','description_seo':description_seo})














#API testimonials
def AboutTes(request):
    lm = int(request.GET['limit'])
    otz = Testimonials.objects.filter(switch = True).order_by('-date')[lm:(lm+5)]

    mass = []
    for a in otz:
        mass.append({
        'name':a.name,
        'date':_date(a.date, "d E Y")+' г.',
        'text':a.text,
        })

    return HttpResponse(str(json.dumps(mass)))





def AboutNewsAll(request):
    try:
        if request.COOKIES['sessionid']:
            lm = int(request.GET['limit'])
            otz = News.objects.all().order_by('-date')[lm:(lm+6)]
    except:
            lm = int(request.GET['limit'])
            otz = News.objects.filter(confirm=True).order_by('-date')[lm:(lm+6)]

    mass = []
    for a in otz:
        mass.append({
        'id':a.id,
        'title':a.title,
        'img':str(a.image),
        'description':a.description,
        'date':_date(a.date, "d E Y")+' г.',
        })

    return HttpResponse(str(json.dumps(mass)))




def LastNews(request):
    otz = News.objects.all().order_by('-date')[:3]
    mass = []
    for a in otz:
        mass.append({
        'id':a.id,
        'title':a.title,
        'date':_date(a.date, "d E Y")+' г.',
        })

    return HttpResponse(str(json.dumps(mass)))





def AboutTesKids(request):
    lm = int(request.GET['limit'])
    otz = TestimonialsKids.objects.filter(switch = True).order_by('-date')[lm:(lm+5)]
    mass = []
    for a in otz:
        mass.append({
        'name':a.name,
        'date':_date(a.date, "d E Y")+' г.',
        'text':a.text,
        })

    return HttpResponse(str(json.dumps(mass)))











def FormTestimonials(request):

    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')

    date = datetime.now().date()
    insert = Testimonials(name = name,date=date,text=message, switch=False)
    insert.save()

    subject, from_email, to = 'Отзыв', 'yarofeevich@cfm.ru', 'kuskova@cfm.ru'
    text_content = 'This is an important message.'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(TmpMail.EMAIL_TEMPLATE_TESTIMONIALS(name,email,message), "text/html")
    msg.send()

    message = 'Спасибо вам за отзыв'

    return render(request,'send_mail.html',{'message':message})






def FormTestimonialsKids(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')

    date = datetime.now().date()
    insert = TestimonialsKids(name = name,date=date,text=message, switch=False)
    insert.save()

    subject, from_email, to = 'Отзыв детского отделения', 'yarofeevich@cfm.ru', 'kuskova@cfm.ru'
    text_content = 'This is an important message.'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(TmpMail.EMAIL_TEMPLATE_TESTIMONIALS(name,email,message), "text/html")
    msg.send()

    message = 'Спасибо вам за отзыв'

    return render(request,'send_mail.html',{'message':message})






def SendEmailForm(request):
    name = request.POST['name']
    post  = request.POST['email']
    message = request.POST['message']
    city = 'Не указано'

    subject, from_email, to = 'Вопрос', 'yarofeevich@cfm.ru', request.POST['doc']
    text_content = 'This is an important message.'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(TmpMail.EMAIL_TEMPLATE_FAQ(name,city,post,message,), "text/html")
    msg.send()

    message = 'Спасибо за письмо'

    return render(request,'send_mail.html',{'message':message})





def FormFaq(request):
    name = request.POST['nameOnline']
    city = request.POST.get('cityOnline',False)
    message = request.POST['messageOnline']
    post  = request.POST['emailOnline']
    insert = Messages(type_message=2,name=name,phone='Отсутствует',post=post,priem='Отсутствует',city=city,message=message,datetime=datetime.now())
    insert.save()

    subject, from_email, to = 'Вопрос', 'yarofeevich@cfm.ru', 'cfm2001@mail.ru' #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    text_content = 'This is an important message.'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(TmpMail.EMAIL_TEMPLATE_FAQ(name,city,post,message,), "text/html")
    msg.send()

    message = 'Спасибо за вопрос'

    return render(request,'send_mail.html',{'message':message})








def FormOnline(request):
    name = request.POST['nameOnline']
    phone = request.POST['phoneOnline']
    post = request.POST['emailOnline']
    date = request.POST['dateOnline']
    priem = request.POST['dayOnline']
    message = request.POST['messageOnline']
    insert = Messages(type_message=1,name=name,phone=phone,post=post,dateOnline=date,priem=priem,city="Отсутствует",message=message,datetime=datetime.now())
    insert.save()

    insert_record = RecordOnline(name=name,phone=phone,post=post,dateOnline=date,priem=priem,message=message,datetime=datetime.now())

    insert_record.save()

    subject, from_email, to = 'Запись', 'yarofeevich@cfm.ru', 'online_cfm@mail.ru'   #_-------------------------------------------------------------------------------------------------------------------------->
    text_content = 'This is an important message.'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(TmpMail.EMAIL_TEMPLATE_ONLINE(name,post,message,phone,date,priem), "text/html")
    msg.send()

    message = 'Ваша запись отправлена'

    return render(request,'send_mail.html',{'message':message})








def FormAnketa(request):

    name = request.POST['nameOnline']
    born = request.POST['bornOnline']
    post  = request.POST['emailOnline']
    phone = request.POST['phoneOnline']
    skype = request.POST['skypeOnline']
    date = request.POST['dateOnline']
    time = request.POST['timeOnline']
    price = request.POST['priceOnline']
    theme  = request.POST['themeOnline']

    subject, from_email, to = 'Запись к психологу', 'yarofeevich@cfm.ru', 'online_cons@cfm.ru'   #_-------------------------------------------------------------------------------------------------------------------------->
    text_content = 'This is an important message.'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])

    msg.attach_alternative(TmpMail.EMAIL_TEMPLATE_ANKETA(name,born,post,phone,skype,date,time,price,theme), "text/html")
    msg.send()

    message = 'Ваша заявка принята'
    return render(request,'send_mail.html',{'message':message})









def FormCommunicate(request):
    name = request.POST['nameOnline']
    phone = request.POST['phoneOnline']
    city = request.POST.get('cityOnline',False)
    message = request.POST['messageOnline']
    post  = request.POST['emailOnline']



    insert = Messages(type_message=3,name=name,phone=phone,post=post,priem='Отсутствует',city=city,message=message,datetime=datetime.now())
    insert.save()


    subject, from_email, to = 'Запись', 'yarofeevich@cfm.ru', 'online_cfm@mail.ru'   #_-------------------------------------------------------------------------------------------------------------------------->
    text_content = 'This is an important message.'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])

    msg.attach_alternative(TmpMail.EMAIL_TEMPLATE_COM(name,city,post,phone,message), "text/html")
    msg.send()

    message = 'Спасибо за письмо'

    return render(request,'send_mail.html',{'message':message})
