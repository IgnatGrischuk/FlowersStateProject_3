import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "flowers_state_project.settings")

app = Celery("flowers_state_project")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'every-1-day': {
        'task': 'flowers_state.tasks.flowers_notifications',
        'schedule': crontab(hour='*/24')
    }
}