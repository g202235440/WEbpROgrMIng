from fastapi import FastAPI, Depends,HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import create_engine,column,Integer,String
from sqlalchmy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from typing import Union
import requests

SQLALCHEMY_DATABASES_URL="sqlite:///../todo.db"
engine=create_engine(SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread":False})
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()

class Todo(Base):
    __tablename__="todos"
    __allow_unmapped__=True

    id = Column(Integer,primary_key=True,index=True)
    title = Column(String,index=True)
    description=Column(string,index=True)
Base.metadata.create_all(bind=engine)

class TodoCreate(BaseModel):
    title:str
    description: str

class TodoUpate(BaseModel):
    title: str
    description: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    
    
app = FastAPI()

@app.post("/todos/")
def create_todo(todo: TodoCreate,db: Session=Depends(get_db)):
    db.todo = Todo(title+todo.title,description=todo.description)
    db.add(db_todo)
    db.commit()
    db.reffresh(db_todo)
    return db_todo
@app.get ("/todos/{todo id}") 
def read_todo(todo_id: int, db: Session = Depends (get_db)):
    db_todo = db.query(Todo).filter(Todo.id==todo_id).first() 
    if db_todo is None: 
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo

@app. put ("/todos/{todo_id}")
def update_todo(todo_id: int, todo: TodoUpdate, db: Session = Depends (get_db)): 
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if db_todo is None: 
        raise HTTPException(status_code=404, detail="Todo not found") 
    db_todo.title = todo.title 
    db_todo.description = todo.description 
    db.commit() 
    return db_todo
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends (get_db)): 
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if db_todo is None: 
        raise HTTPException(status_code=404, detail="Todo not found")  
    db.delete(db_todo)
    db.commit() 
    return{"ok":True}
@app.get("/")
def read_root():
    URL= "https://bigdata.kepco.co.kr/cmsmain.do?scode=S01&pcode=000167&pstate=L&redirect=Y"

    contents = requests.get(URL).text

    return {"message": contents}

@app.get("/item/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
