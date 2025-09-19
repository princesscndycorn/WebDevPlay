from celery import Celery
import os
celery_app = Celery(
	"myapp",
	broker=os.environ.get("BROKER_URL"),
	backend=os.environ.get("BROKER_URL"),
	include=['tasks']
)
#celery_app.config_from_object("celery_config")

# Discover tasks dynamically, without force, it wasn't finding the tasks.
celery_app.autodiscover_tasks(["tasks.rock", "tasks.fred"],force=True)