from fastapi import APIRouter, Header
from celery_app import celery_app
from celery.result import AsyncResult
from tasks.rock.tasks import add

router = APIRouter(prefix="/bingo", tags=["bingo"])

@router.post("/submit")
def queue_add(x: int, y: int):
    task = add.delay(x, y)
    return {"task_id": task.id}


@router.post("/info")
def queue_add(x: int, y: int):
    task = multiply.delay(x, y)
    return {"task_id": task.id}


@router.get("/status")
def status_job(jobid: str):
    results = AsyncResult(jobid, app=celery_app)
    return {"State": f"{results.status}"}


@router.get("/results")
def return_results(jobid: str):
    results = AsyncResult(jobid, app=celery_app)
    if results.status == 'SUCCESS':
        return {
            "STATE": "SUCCESS",
            "RESULTS": results.get()
        }
    else:
        return {"State": f"{results.status}"}
