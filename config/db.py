from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

def init_app(app: Flask):
    db.init_app(app)
    app.db = db

    from models.student_model import StudentModel
        
    with app.app_context():
        db.drop_all()
        db.create_all()
