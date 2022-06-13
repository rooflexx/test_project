from django.contrib.auth import get_user_model

from config import celery_app



@celery_app.task()
def add(x, y):
    return x + y
