from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.orm import Session

import api.models.table as task_model
import api.schemas.task as task_schema


def create_task(db: Session,task_create:task_schema.TaskCreate)->task_model.Task:
    task=task_model.Task(**task_create.dict())
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_tasks_with_done(db: Session)->list[tuple[int,str]]:
    result:Result = db.execute(
        select(
            task_model.Task.id,
            task_model.Task.title,
            task_model.Task.crno,
            task_model.Task.year, 
            task_model.Task.enpSaleAmt,
            task_model.Task.enpBzopPft,
            task_model.Task.iclsPalClcAmt,
            task_model.Task.enpCrtmNpf,
            task_model.Task.enpTastAmt,
            task_model.Task.enpTdbtAmt,
            task_model.Task.enpTcptAmt,
            task_model.Task.enpCptlAmt,
            task_model.Task.fnclDebtRto,
        )
    )
    
    return result.all()


