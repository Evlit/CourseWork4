# модель Users - пользователи
from marshmallow import Schema, fields
from setup_db import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100))
    surname = db.Column(db.String(100))
    favorite_genre = db.Column(db.Integer, db.ForeignKey("genres.id"))
    genre = db.relationship("Genre")


class UserSchema(Schema):
    id = fields.Int(required=True)
    email = fields.Str(required=True)
    name = fields.Str(required=True)
    surname = fields.Str()
    favorite_genre = fields.Int()
