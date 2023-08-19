import django.db
import mysql.connector
from myapp1.models import Articles, NewTab
from myapp1.forms import Comment


def index_data(cat):


    print('hello' + str(cat))
    #if cat == '':
    #    print("NONNONO")
    #    art = Articles.objects.all()
    #if cat == 'phil':
    #    print("phil")
    #elif cat == 'art':
    #    print("art") 
    #elif cat == 'scince':
    #    print("scince")
    #elif cat == 'rel':
    #    print("rel")
#
    #return art




def post_data(id):

    print('in here')
    # ОБРАЩЕНИЕ к БД...
    # получение данных статьи из БД
    full_art = Articles.objects.get(id=id)

    # так же можно создать форму и ее запаковать и кинуть в шаблон
    comment = Comment()

    # (пакуем ве в словарь если надо отдельно)

    # отправка данных конкретной статьи и полей формы для отрисовки в шаблон
    return full_art, comment

#def phil_data(cat):
#
#    art = Articles.objects.all()
#
#    return art
#
#
#def art_data(cat):
#
#    art = Articles.objects.all()
#
#    return art
#
#
#def scince_data(cat):
#
#    art = Articles.objects.all()
#
#    return art
#
#
#def rel_data(cat):
#
#    art = Articles.objects.all()
#
#    return art



#hello
