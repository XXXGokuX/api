from database import Base
from sqlalchemy import Column,Integer,String,DateTime,func


class User(Base):
    __tablename__= "allUsers"

    id= Column(Integer,primary_key=True,nullable=False)
    username= Column(String(255),nullable=False)
    password= Column(String(255),nullable=False)
    created_at = Column(DateTime, default=func.now())

    