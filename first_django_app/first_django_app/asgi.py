"""
ASGI config for first_django_app project.
ASGI (Asynchronous Server Gateway Interface) is spiritual successor to WSGI,
intended to provide a standard interface between async-capable Python web servers, frameworks, and applications.

Where WSGI provided a stanard for synchronous Python apps, ASGI provides one for both asynchronous and synchronous applications. 

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_django_app.settings')

application = get_asgi_application()
