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

# app.conf.broker_use_ssl = {
#     'ssl_cert_reqs': 'required',
#     'ssl_ca_certs': '/app/redis.crt',
#     'ssl_certfile': '/app/client.crt',
#     'ssl_keyfile': '/app/client.key',
# }

app.conf.broker_use_ssl = {
    'ssl_certfile': os.environ.get("REDIS_CLIENT_CERT"),
    'ssl_keyfile': os.environ.get("REDIS_CLIENT_KEY"),
    'ssl_ca_certs': os.environ.get("REDIS_CA_CERT"),
    'ssl_cert_reqs': 'none',
}
app.conf.redis_backend_use_ssl = app.conf.broker_use_ssl


@app.task(queue="add")
def add(x, y):
    return x + y


@app.task(queue="multiply")
def multiply(x, y):
    return x * y

