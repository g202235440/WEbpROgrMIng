from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


from api.db import Base
import requests

class Task(Base):
    __tablename__="stock"

    id=Column(Integer, primary_key=True)
    title = Column(String(1024))

    done = relationship("Done",back_populates="stock",cascade="delete")

class Done(Base):
    __tablename__="Done"

    id=Column(Integer,ForeignKey("stock.id"),primary_key=True)
    
    stock = relationship("Task",back_populates="done")
