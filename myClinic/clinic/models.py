from enum import Enum as PyEnum
from sqlalchemy import DateTime, Enum, Column, Integer, String, Float, Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship
from clinic import app, db, utils
from datetime import datetime, date
from flask_login import UserMixin

class Gender(PyEnum):
    MALE = 'male'
    FEMALE = 'female'

class UserRole(PyEnum):
    ADMIN = 'admin'
    PATIENT = 'patient'

class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    avatar = Column(String(100))
    email = Column(String(50), unique=True)
    user_role = Column(Enum(UserRole), default=UserRole.PATIENT)
    status = Column(Boolean, default=True)
    gender = Column(Enum(Gender))

    def __str__(self):
        return self.name

class Admin(db.Model):
    __tablename__ = 'admin'
    id = Column(Integer, ForeignKey(User.id), primary_key=True)



class Patient(db.Model):
    __tablename__ = 'patient'
    id = Column(Integer, ForeignKey(User.id), primary_key=True)


if __name__== '__main__':
    with app.app_context():
        db.drop_all()  # Xóa tất cả các bảng
        db.create_all()
        db.session.commit()
        #test
        admin1 = User(
            name = 'admin1',
            username = 'admin1',
            password = '123',
            avatar = 'https://res.cloudinary.com/dmz9kuzue/image/upload/v1732014605/samples/dessert-on-a-plate.jpg',
            email = '2251010077phuong@ou.edu.vn',
            user_role = UserRole.ADMIN,
            gender = Gender.FEMALE
        )
        patient1 = User(
            name='patient1',
            username='patient1',
            password='123',
            avatar='https://res.cloudinary.com/dmz9kuzue/image/upload/v1732014605/samples/dessert-on-a-plate.jpg',
            email='nglhongphuong@gmail.com',
            user_role=UserRole.PATIENT,
            gender=Gender.FEMALE
        )
        patient2 = User(
            name='patient2',
            username='patient2',
            password=(utils.hash_password('123')),
            avatar='https://res.cloudinary.com/dmz9kuzue/image/upload/v1732014605/samples/dessert-on-a-plate.jpg',
            email='vvui3256@gmail.com',
            user_role=UserRole.PATIENT,
            gender=Gender.MALE
        )
        db.session.add_all([admin1, patient1, patient2])
        db.session.commit()



