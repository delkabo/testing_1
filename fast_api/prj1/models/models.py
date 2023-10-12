from typing import Any, List, Union

from pydantic import BaseModel

class User(BaseModel):
    name: str
    id: int
    is_adult: bool

class Feedback(BaseModel):
    name: str
    message: str

class UserCreate(BaseModel):
    name: str
    email: str
    age: int
    is_subscribed: bool = False

class SampleProducts(BaseModel):
    product_id: int
    name: str
    category: str
    price: float
