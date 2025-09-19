from fastapi import FastAPI
from routers import bluey, bingo, scoobydoo

app = FastAPI(tags=["main"])

# Include routers
app.include_router(bluey.router)
app.include_router(bingo.router)
app.include_router(scoobydoo.router)


@app.get("/hello")
def hello():
    return {"message": "Hellow World?"}