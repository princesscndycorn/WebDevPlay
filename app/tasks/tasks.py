from celery import Celery
from celery import states
from celery.utils.log import get_task_logger
import time
import os

logger = get_task_logger(__name__)

app = Celery(
    __name__,
    broker=os.environ.get("CELERY_BROKER"),
    backend=os.environ.get("CELERY_BACKEND"),
    include=['tasks']
)

app.conf.broker_use_ssl = {
    'ssl_cert_reqs': 'required',
    'ssl_ca_certs': '/app/redis.crt',
}
app.conf.redis_backend_use_ssl = app.conf.broker_use_ssl


@app.task(queue="add")
def add(x, y):
    return x + y


@app.task(queue="multiply")
def multiply(x, y):
    return x * y

