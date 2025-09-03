from pydantic import BaseModel, Field, validator
from typing import Optional, List
import re
from datetime import datetime

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

class ContainerBase(BaseModel):
    container_number: str = Field(..., min_length=11, max_length=11)
    cost: float = Field(..., gt=0)
    
    @validator('container_number')
    def validate_container_number(cls, value):
        if not re.match(r'^[A-Z]{3}U\d{7}$', value):
            raise ValueError('Номер контейнера должен быть в формате ABCU0123456')
        return value.upper()
    
    @validator('cost')
    def validate_cost(cls, value):
        return round(value, 2)

class ContainerCreate(ContainerBase):
    pass

class Container(ContainerBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

class ContainerResponse(BaseModel):
    id: int
    container_number: str
    cost: float
    created_at: datetime

class ContainerListResponse(BaseModel):
    containers: List[ContainerResponse]
    total: int

class ErrorResponse(BaseModel):
    detail: str

class ValidationErrorResponse(BaseModel):
    detail: List[dict]