from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique = True, nullable = False)
    username = db.Column(db.String(150), nullable = False)
    hash_password = db.Column(db.String(150), nullable = False)

    def __init__(self, username, password, email):
        self.username = username
        self.email = email
        self.hash_password = generate_password_hash(password, method= "sha256")
        

class Client(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    last_name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), nullable = False)
    phone = db.Column(db.String(20), nullable = False)
    vehicles = db.relationship('Vehicle', backref = "client")
    date = db.Column(db.DateTime(timezone = True), default = func.now())
    
    def __init__(self, name,last_name,email,phone):
        self.name = str(name).strip().title()    
        self.last_name = str(last_name).strip().title()    
        self.email = str(email).strip()   
        self.phone = str(phone).replace("(","").replace(")","").replace("-","").replace(" ","").replace("+","").strip()

    
class Model(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    model = db.Column(db.String(50), nullable = False)
    vehicles = db.relationship('Vehicle', backref = "model")
    
    def __init__(self, model):
        self.model = str(model).strip().title()

class Color(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    color = db.Column(db.String(100), nullable = False)
    hex_code = db.Column(db.String(7), nullable = False)
    vehicles = db.relationship('Vehicle', backref = "color")
    
    def __init__(self, color, hex_code):
        self.color = str(color).strip().title()
        self.hex_code = str(hex_code)
        
class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    model_id = db.Column(db.Integer, db.ForeignKey('model.id'))
    color_id = db.Column(db.Integer, db.ForeignKey('color.id'))
    