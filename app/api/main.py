from fastapi import FastAPI
from tasks import add, multiply

app = FastAPI()

@app.post("/add")
def queue_add(x: int, y: int):
    task = add.delay(x, y)
    return {"task_id": task.id}

@app.post("/multiply")
def queue_add(x: int, y: int):
    task = multiply.delay(x, y)
    return {"task_id": task.id}