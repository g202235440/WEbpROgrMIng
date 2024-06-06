from sqlalchemy.orm import Session
import api.cruds.task as task_crud  # assuming your CRUD functions are in this module

def kell(db: Session):#알고리즘으로 계산후 결과 값을 반환해주는 
    # Get all tasks with 'done' status
    tasks = task_crud.get_tasks_with_done(db)
    fourth_task = tasks[3][1]##3번째 행 2번째 열 인 회사이름이 저장 된 걸것임
    return fourth_task
    
      # 0-based index, so the fourth element is at index 3
        