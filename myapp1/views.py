from . forms import Comment, AddForm
from django.template.response import TemplateResponse
import traceback
from django.http import HttpResponse, HttpResponseRedirect
import django.db
from . models import Articles, NewTab
from django.shortcuts import render, HttpResponseRedirect, reverse
import mysql.connector
from myapp1.services import post_data, index_data

#from django.template.response import TemplateResponse
#from django.http import HttpResponse
#from django.shortcuts import render

 
def index(request, cat=None):

    index_data(5)

    # берем из БД все статьи
    if cat == None:
        arts = Articles.objects.all()
        print(arts)
    else:
        arts = Articles.objects.filter(post_category=cat)

    # вывод списка всех статей
    return render(request, 'myapp1/index.html', {'arts': arts})









def sender(request):

    # получаем комменатрий по ПОСТ    
    comm = str(request.POST.get('message'))
    print('666666666666666666666666666666666666666666', comm)
    #Articles.objects.filter(id=2).update(post_autor=comm)
    nt = NewTab()
    nt.name = comm
    nt.save()
    # заносим в базу
    #a = Articles.objects.all()

    return HttpResponseRedirect('/')








def indx(request):

    data = NewTab.objects.all()
    frm = AddForm()

    return render(request, 'myapp1/tst.html', {'data': data, 'frm': frm})






def new_label(request):

    print('***********', request.POST.get('pole'))
    nt = NewTab()
    nt.name = str(request.POST.get('pole'))
    nt.save()

    return HttpResponseRedirect(reverse('indx'))



def edit(request):

    nt = NewTab.objects.get(id=id)

    return render(request, 'myapp1/tst.html', {'nt': nt})




def delete(request, id):
    
    nt = NewTab.objects.get(id=id)
    nt.delete()
    return HttpResponseRedirect(reverse('indx'))
    
    


















# вывод конкретной статьи по ID и формы для комментов
def post(request, id=None):
    
    #full_art, comment = post_data(id)

    # ОБРАЩЕНИЕ к БД...
    # получение данных статьи из БД
    full_art = Articles.objects.get(id=id)
#
    # так же можно создать форму и ее запаковать и кинуть в шаблон
    comment = Comment()

    # (пакуем ве в словарь если надо отдельно)

    # отправка данных конкретной статьи и полей формы для отрисовки в шаблон
    return render(request, 'myapp1/post.html', {'full_art': full_art, 'comment': comment})




def about(request):

    print('dsfffffffffffffff')
    # здесь какая то логика, а затем отправка данных в шаблон
    return render(request, 'myapp1/about.html')




def reg(request):


    return render(request, 'myapp1/about.html')





def mod(request):


    # получаем все данные
    a = Articles.objects.all()

    # a = Articles.objects.order_by('post_title')

    # john = NewTab(name='John')
    # john.save()

    # выводим их в браузер
    return render(request, 'new_form.html', {'a': a})









