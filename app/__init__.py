from flask_restx import Api,Resource,marshal,fields
from flask import Flask
import os
from .models import Meal
from .exts import db
from .api import api_bp
from .ui import ui_bp

basedir=os.path.dirname(os.path.realpath(__file__))

def create_app():
    app=Flask(__name__,static_folder='./static')

    app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///'+os.path.join(basedir,'api.db')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

    db.init_app(app)


    app.register_blueprint(api_bp,url_prefix='/api')
    app.register_blueprint(ui_bp,url_prefix='/')

    @app.shell_context_processor
    def make_shell_context():
        return {
            'app':app,
            'api':api,
            'db':db,
            'Meal':Meal
        }

    return app
