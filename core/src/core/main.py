# Project Ignition sequence

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.routes.editor import editor_route



import uvicorn


app = FastAPI()

app.include_router(editor_route)

# Enabling cors origin requests
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
