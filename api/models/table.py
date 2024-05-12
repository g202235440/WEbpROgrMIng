from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from api.db import Base

class Task(Base):
    __tablename__="stock"

    id=Column(Integer, primary_key=True)
    title = Column(String(1024))
