"""
WSGI config for first_django_app project.

WSGI is the Web Server Gateway Interface.
It is a specification that describes a web server communicates with web applications,
and how web applications can be chained togehter to process one request.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_django_app.settings')

application = get_wsgi_application()
