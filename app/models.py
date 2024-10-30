from flask_login import UserMixin       
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Employee(db.Model, UserMixin):
    __tablename__ = 'employees'

    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String(100), nullable=False)
    employee_number = db.Column(db.Integer , nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)