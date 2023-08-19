print('|11|in_proj START D:/djpro/myapp1/urls.py')
from django.urls import path, re_path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

#from django.contrib import admin
#from django.urls import path, re_path, include
#from django.conf import settings
#from django.conf.urls.static import static
#from myapp1 import views

print('---myapp1.URLS.py')

#print('path_from_myapp1.urls.py', path('', views.index, name='main'))
#print('path_from_myapp1.urls.py', path('phil', views.index, name='phil'))

urlpatterns = [

    # для корня
    path('', views.index, name='home'),

    # для корня с парметром
    path('<str:cat>', views.index, name='home'),
    
    # для отдельной статьи
    re_path(r'post/(?P<id>\d+)', views.post, name='post'),
    
    # для регистрации
    path('reg/', views.reg, name='reg'),
    
    # о нас 
    path('about/', views.about, name='about'),



    # отправка сообщений
    path('sender/', views.sender, name='sender'),

    # отправка статьи ...
    # отправка лайки и тд ...
 


    path('mod/', views.mod, name='mod'),



    path('indx/', views.indx, name='indx'),
    path('new_label/', views.new_label, name='new_label'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),




]


print('|11|in_proj END D:/djpro/myapp1/urls.py')


