from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
router = APIRouter()

import api.cruds.task as task_crud
from api.db import get_db
import api.schemas.task as task_schema
from api.api.request import get_data

@router.get("/")
def hello():
    return{"message":"hello"}
    
@router.post("/tasks", response_model=List[task_schema.TaskCreateResponse])
async def create_task(db: Session = Depends(get_db)):
    created_tasks = []
    for p in range(5,10):
        #data = get_data('http://apis.data.go.kr/1160100/service/GetStockSecuritiesInfoService/getStockPriceInfo',p,1,'itmsNm')
        data = get_data('http://apis.data.go.kr/1160100/service/GetCorpBasicInfoService_V2/getCorpOutline_V2',p,1,'corpNm')
        data2 = get_data('http://apis.data.go.kr/1160100/service/GetCorpBasicInfoService_V2/getCorpOutline_V2',p,1,'crno')
        task_body = task_schema.TaskCreate(title=data,crno=data2)
        created_task = task_crud.create_task(db, task_body)
        created_tasks.append(created_task)
    return created_tasks

@router.get("/tasks",response_model=list[task_schema.Task])
async def list_task(db:Session = Depends(get_db)):
    return task_crud.get_tasks_with_done(db)
