from enum import Enum as UserEnum
from sqlalchemy import DateTime,Enum, Column,Integer,String,Float,Boolean,ForeignKey,Date
from sqlalchemy.orm import relationship
from clinic import app, db
from datetime import datetime, date
from flask_login import UserMixin

class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)


class UserRole(UserEnum):
    ADMIN = 1
    USER = 2

class User(BaseModel, UserMixin):
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    avatar = Column(String(100))
    email = Column(String(50))
    user_role = Column(Enum(UserRole), default=UserRole.USER)

    def __str__(self):
        return self.name



if __name__== '__main__':
    with app.app_context():
        db.create_all()
        db.session.commit()
