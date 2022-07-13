from flask import Flask
from flask import Blueprint
from environs import Env
from config import db
import views

bp = Blueprint('escola', __name__, url_prefix='/api')

def create_app() -> Flask:
    app = Flask(__name__)
    env = Env()
    env.read_env()
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://anderson:1234@postgres:5432/escoladb'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JSON_SORT_KEYS"] = False
    
    db.init_app(app)
    views.init_app(app)
    return app