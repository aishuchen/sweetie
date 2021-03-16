from fastapi import FastAPI
from routers import sweetie

app = FastAPI()
app.include_router(sweetie.router)


@app.get("/")
def index():
    return {"message": "盲生你发现了华点"}
