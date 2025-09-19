from fastapi import APIRouter, Header
from celery.result import AsyncResult
from celery_app import celery_app
from tasks.rock.tasks import add

router = APIRouter(prefix="/bluey", tags=["bluey"])

#task = celery_app.send_task("task_projects.project1.tasks.add", args=[x, y])

@router.get("/add")
def queue_add(x: int, y: int):
    #celery_app.send_task("task_projects.project1.tasks.add", args=[x, y])
    #task = add.delay(x, y)
    return {"task_id": "Beta"}


@router.get("/multiply")
def queue_add(x: int, y: int):
    # task = multiply.delay(x, y)
    return {"task_id": "Beta"}
