import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTING_MODULE',
                      'flowers_state_project.settings')

app = Celery("flowers_state_project")
app.config_from_object("django.conf:settings", namespace='CELERY')





