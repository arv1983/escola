
from flask import Flask

def init_app(app: Flask):
    from .student_view import bp as student
    app.register_blueprint(student)

