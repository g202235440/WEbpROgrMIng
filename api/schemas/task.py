from pydantic import BaseModel,Field

class TaskBase(BaseModel):
    title : str | None = Field(None, example="안녕하세요")

class TaskCreate(TaskBase):
    crno : str | None = Field(None, example="00000000")
    year : int | None = Field(None, example="00000000")
    enpSaleAmt : float | None = Field(None, example="00.000000")
    enpBzopPft : float | None = Field(None, example="00.000000")
    iclsPalClcAmt : float | None = Field(None, example="00.000000")
    enpCrtmNpf : float | None = Field(None, example="00.000000")
    enpTastAmt: float | None = Field(None, example="00.000000")
    enpTdbtAmt : float | None = Field(None, example="00.000000")
    enpTcptAmt : float | None = Field(None, example="00.000000")
    enpCptlAmt : float | None = Field(None, example="00.000000")
    fnclDebtRto : float | None = Field(None, example="00.000000")
   
   #사실 다 나누는게 좋을것같지만 그건 귀찮으니 그냥 대충 하자


class TaskCreateResponse(TaskCreate):
    id: int
    class Config:
        orm_mode = True

class Task(TaskBase):#여기서 title만 가져가는건 그 데이터는 저장되어있다는 뜻
    id:int
    class Config:
        orm_mode=True


