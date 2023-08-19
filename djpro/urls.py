print('|4|in_proj START D:/djpro/djpro/urls.py')

"""
URL configuration for djpro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from myapp1 import views

print('---URLS.py')

#print('path_from_urls.py', path('admin/', admin.site.urls))
#print('path_from_urls.py', re_path(r'test/(?P<id>\d+)', views.test))
#print('path_from_urls.py', path('test/', views.test))
#print('path_from_urls.py', path('', include('myapp1.urls')))



urlpatterns = [
    path('admin', admin.site.urls), 
    path('', include('myapp1.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



print('|4|in_proj END D:/djpro/djpro/urls.py')
