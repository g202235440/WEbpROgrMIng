from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()

import api.cruds.task as task_crud
from api.db import get_db
import api.schemas.task as task_schema

@router.get("/")
def hello():
    return{"message":"hello"}
    

@router.post("/tasks",response_model=task_schema.TaskCreateResponse)
async def create_task(task_body:task_schema.TaskCreate,db:Session = Depends(get_db)):
    return task_crud.create_task(db,task_body)

@router.get("/tasks",response_model=list[task_schema.Task])
async def list_task(db:Session = Depends(get_db)):
    return task_crud.get_tasks_with_done(db)
