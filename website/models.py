from . import db
import datetime
from flask_login import UserMixin
from sqlalchemy.sql import func
# ---------------------------------------------------------------
# MODELO NOTES
# ---------------------------------------------------------------
# class Note(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     data = db.Column(db.String(10000))
#     date = db.Column(db.DateTime(timezone=True), default=func.now())
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
# ---------------------------------------------------------------
# MODELO USUARIOS
# ---------------------------------------------------------------
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    produtos = db.relationship('Produto',backref='produto')
# ---------------------------------------------------------------
# MODELO CLIENTES
# ---------------------------------------------------------------    
class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fone = db.Column(db.String(150))
    data_criacao = db.Column(db.DateTime(timezone=True), default=func.now())
    nome = db.Column(db.String(150))    
# ---------------------------------------------------------------
# MODELO PRODUTOS
# ---------------------------------------------------------------    
class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String(150))
    descricao = db.Column(db.String(150))
    tamanho = db.Column(db.String(150))
    valor = db.Column(db.Float)
    data_criacao = db.Column(db.DateTime(timezone=True), default=func.now())
    criador = db.Column(db.Integer, db.ForeignKey('user.id'))


