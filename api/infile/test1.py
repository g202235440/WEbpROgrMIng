from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()

import api.cruds.task as task_crud
from api.db import get_db
import api.schemas.task as task_schema
from api.api.request import get_data

@router.get("/")
def hello():
    return{"message":"hello"}
    

#@router.post("/tasks",response_model=task_schema.TaskCreateResponse)
#async def create_task(task_body:task_schema.TaskCreate,db:Session = Depends(get_db)):
#    return task_crud.create_task(db,task_body)

@router.post("/tasks",response_model=task_schema.TaskCreateResponse)
async def create_task(db:Session = Depends(get_db)):
    for p in range(1, 6):
        data =get_data(p,1,'crno')
        task_body = task_schema.TaskCreate(title=data)
        return task_crud.create_task(db,task_body)


@router.get("/tasks",response_model=list[task_schema.Task])#TaskCreateResponse로 바꾸기
async def list_task(db:Session = Depends(get_db)):
    return task_crud.get_tasks_with_done(db)
