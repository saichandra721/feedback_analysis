import datetime
from sqlalchemy import Column, Integer, String, JSON, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    password = Column(String)
    account = Column(String)
    faculty = relationship("Faculty", back_populates='account')
    student = relationship("Student", back_populates='account')



class Faculty(Base):
    __tablename__ = "faculty"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    subject = Column(String)
    score = Column(Integer)
    feed = Column(JSON)
    user_id = Column(Integer, ForeignKey('user.id'))
    account = relationship("User", back_populates='faculty')
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.datetime.utcnow())

class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    feed = Column(JSON)
    user_id = Column(Integer, ForeignKey('user.id'))
    account = relationship("User", back_populates='student')
    created_at = Column(DateTime, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.datetime.utcnow())

