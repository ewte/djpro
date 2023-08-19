print('|2|in_proj START D:/djpro/djpro/asgi.py')
"""
ASGI config for djpro project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""
print('start ASGI.py')
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djpro.settings')

application = get_asgi_application()
print('|2|in_proj END D:/djpro/djpro/asgi.py')
