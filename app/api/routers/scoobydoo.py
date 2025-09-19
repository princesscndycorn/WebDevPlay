from fastapi import APIRouter, Header
from celery.result import AsyncResult
from celery_app import celery_app
from tasks.rock.tasks import add

router = APIRouter(prefix="/scooby", tags=["scooby"])

@router.get("/velma")
def queue_add(x: int, y: int):
    return {"task_id": "Beta"}


@router.post("/daphnie")
def queue_add(x: int, y: int):
    return {"task_id": "Beta"}
