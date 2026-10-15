# Project Ignition sequence
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from vizion-endpoint"}


def ignite():
    uvicorn.run(
            "core.main:app",
            host="127.0.0.1",
            port=8000,
            reload=True
            )
