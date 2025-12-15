from fastapi import FastAPI
from app.pages.router import router as router_pages
import os
from typing import Optional

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "this is a custom message!"}