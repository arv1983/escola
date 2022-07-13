from config.db import db
from sqlalchemy import Column, String, Integer,DateTime
from validate_docbr import CPF

from services.mask import Masks

class StudentModel (db.Model):
    __tablename__ = "Student"
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(255), nullable=False)
    cpf = Column('cpf', String(11), nullable=False, unique=True)
    email = Column('email', String(255), nullable=False)
    phone_number = Column('phone_number', String(11), nullable=False)
    created_at = Column('created_at', DateTime)
           
    def serialized(self):
        data = {
            "id": self.id,
            "name": self.name,
            "cpf": CPF().mask(self.cpf),
            "email": self.email,
            "phone": Masks.phone(self.phone_number),
            "created_at": self.created_at.strftime('%d/%m/%Y - %H:%M')
        }
        
        return data

    def get_all_students():
        
        users = []
        for user in StudentModel.query.all():
            users.append(StudentModel.serialized(user))
        return users

    def get_student_by_cpf(cpf_user: str):
        return StudentModel.query.filter_by(cpf=cpf_user).first()

    def search_student_by_name(search: str):
        search = '%{}%'.format(search)

        users = []
        for user in StudentModel.query.filter(StudentModel.name.like(search)).all():
            users.append(StudentModel.serialized(user))
        return users

    def get_student_by_id(id: str):
        return StudentModel.query.filter_by(id=id).first()
    


    
