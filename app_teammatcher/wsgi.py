"""
WSGI config for studentmatcher project.
"""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app_teammatcher.settings")

application = get_wsgi_application()
