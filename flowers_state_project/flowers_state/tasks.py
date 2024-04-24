from celery import shared_task
from django.core.mail import send_mail
import time
from django.conf import settings
from users.models import CustomUser


@shared_task
def some_task():
    time.sleep(5)
    return 'ABOBA'


@shared_task
def flowers_notifications():
    users = CustomUser.objects.filter(is_notification_required=True)

    for user in users:
        send_mail(
            'Don\'t forget!',
            f"Time to watering flowers!",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email]
        )