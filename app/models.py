from flask_login import UserMixin
from . import db

class Folder(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    col = db.Column(db.String(10000))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

class User(db.Model, UserMixin):
    _id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(100))
