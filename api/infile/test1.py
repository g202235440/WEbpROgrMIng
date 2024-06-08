from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
router = APIRouter()

import api.cruds.task as task_crud
from api.db import get_db
import api.schemas.task as task_schema
from api.api.request import get_data, get_data2
from api.infile.algorithm import kell

@router.get("/")
def hello():
    return{"message":"hello"}
    
@router.post("/tasks", response_model=List[task_schema.TaskCreateResponse])
async def create_task(db: Session = Depends(get_db)):
    created_tasks = []
    for p in [30, 40, 50, 60, 70]:
        url2='http://apis.data.go.kr/1160100/service/GetFinaStatInfoService_V2/getSummFinaStat_V2'
        #data = get_data('http://apis.data.go.kr/1160100/service/GetStockSecuritiesInfoService/getStockPriceInfo',p,1,'itmsNm')
        data2 = get_data(url2,p,1,'crno')
        data = get_data2('http://apis.data.go.kr/1160100/service/GetCorpBasicInfoService_V2/getCorpOutline_V2?&pageNo=1&numOfRows=1&resultType=json&serviceKey=XjAOulAs6VTDHZEFyeermCWZGMt05tyiPeVEpWTocYYwFyMCMEKDr4ktytwl3n3HvLasZJWkO%2FN4JA1pCBGb0A%3D%3D','corpNm',data2)
        data3 = get_data(url2,p,1,'bizYear')
        data4 = get_data(url2,p,1,'enpSaleAmt')
        data5 = get_data(url2,p,1,'enpBzopPft')
        data6 = get_data(url2,p,1,'iclsPalClcAmt')
        data7 = get_data(url2,p,1,'enpCrtmNpf')
        data8 = get_data(url2,p,1,'enpTastAmt')
        data9 = get_data(url2,p,1,'enpTdbtAmt')
        data10 = get_data(url2,p,1,'enpTcptAmt')
        data11 = get_data(url2,p,1,'enpCptlAmt')
        data12 = get_data(url2,p,1,'fnclDebtRto')
        task_body = task_schema.TaskCreate(title=data,crno=data2,year=data3,enpSaleAmt=data4,enpBzopPft=data5,iclsPalClcAmt=data6,enpCrtmNpf=data7,enpTastAmt=data8,enpTdbtAmt=data9,enpTcptAmt=data10,enpCptlAmt=data11,fnclDebtRto=data12)
        created_task = task_crud.create_task(db, task_body)
        created_tasks.append(created_task)
    return created_tasks
## 여기서 회사이름은 crno랑 관계가 없으므로 나중에 매핑을 해야함 부터의 값이랑 전혀 관계가 없음 따라서 할거면 
@router.get("/tasks",response_model=list[task_schema.Task])
async def list_task(db:Session = Depends(get_db)):
    tasks = task_crud.get_tasks_with_done(db)  # 0-based index, so the fourth element is at index 3
    return tasks

@router.get("/task")
async def result(db:Session = Depends(get_db)):
    result=kell(db)
    return result