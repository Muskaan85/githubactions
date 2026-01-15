from fastapi import FastAPI
import os

app = FastAPI()


@app.get("/")
def home():
    return {
        "status": "ok",
        "message": "FastAPI Production App is Live "
    }


@app.get("/health")
def health():
    return {"health": "healthy"}
