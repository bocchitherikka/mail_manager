from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mail_manager.settings')

app = Celery('mail_manager')

app.config_from_object('django.conf:settings')
app.conf.broker_url = 'pyamqp://guest:guest@localhost//'

app.autodiscover_tasks(['newsletter'])
