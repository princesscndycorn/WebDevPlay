

from celery_app import celery_app

@celery_app.task(queue="scoob")
def add(x, y):
    return x + y

@celery_app.task(queue="scoob")
def mul(x, y):
    return x * y