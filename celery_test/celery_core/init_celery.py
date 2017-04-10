from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_test.settings')
app = Celery('app')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('celery_test.celery_core.celery_config')   # django.conf:settings