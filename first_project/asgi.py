"""
ASGI config for first_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

application = get_asgi_application()



# def factorial(num):
#     var = 1
#     for i in range(2,num+1):
#         var*=i
#     print(var)
# factorial(5)      

# add few lines in this file