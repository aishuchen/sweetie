from fastapi import FastAPI
from routers import sweetie

app = FastAPI()
app.include_router(sweetie.router)


@app.get("/")
def index():
    return {"hello": "word"}
