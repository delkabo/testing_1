# main.py

from fastapi import FastAPI
from datetime import datetime
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, world"}

@app.get("/custom")
def read_custom_message():
    return {"message": "This is a custom message!"}

class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None = None
    friends: list[int] = []

external_data = {
    "id": "123",
    "signup_ts": "2117-06-01 12:22",
    "friends": [1, "2", b"3"],
}

user = User(**external_data)
print(user)
print(user.id)