from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
import os
from os.path import join, dirname


db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'views.login'

def create_app():
    app = Flask(__name__)
    
    
    config_type = os.getenv('CONFIG_TYPE', default='config.Dev')
    app.config.from_object(config_type)

    
    db.init_app(app)
    login_manager.init_app(app)
    
    from .models import Client, Vehicle, Model, Color, User
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.filter(User.id == int(id)).first()
    
    from .views import views
    
    app.register_blueprint(views, url_prefix = '/')
    
    with app.app_context():
        db.create_all()

    return app

