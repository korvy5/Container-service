from fastapi import FastAPI, Depends, HTTPException, status
from typing import List, Optional

from app import crud, auth
from app.schemas import Container, ContainerCreate, ContainerResponse
from app.database import get_db_connection

app = FastAPI(
    title="Container Service API",
    description="API для учета контейнеров",
    version="1.0.0"
)

@app.get("/api/containers", response_model=List[Container])
async def get_containers(
    q: Optional[str] = None,
    current_user: dict = Depends(auth.get_current_user)
):
    try:
        containers = crud.get_containers(search=q)
        return containers
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/containers/by-cost", response_model=List[Container])
async def get_containers_by_cost(
    cost: Optional[float] = None,
    min_cost: Optional[float] = None,
    max_cost: Optional[float] = None,
    current_user: dict = Depends(auth.get_current_user)
):
    try:
        containers = crud.get_containers_by_cost(exact=cost, min_cost=min_cost, max_cost=max_cost)
        return containers
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/containers", response_model=Container)
async def create_container(
    container: ContainerCreate,
    current_user: dict = Depends(auth.get_current_user)
):
    try:
        new_container = crud.create_container(container)
        return new_container
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "ok"}