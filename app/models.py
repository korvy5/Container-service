# app/models.py - теперь только для данных, связанных с БД
from typing import TypedDict
from datetime import datetime

class User(TypedDict):
    id: int
    username: str
    password_hash: str
    created_at: datetime

class Container(TypedDict):
    id: int
    container_number: str
    cost: float
    created_at: datetime