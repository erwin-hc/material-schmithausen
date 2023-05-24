from . import db
import datetime
from flask_login import UserMixin
from sqlalchemy.sql import func
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

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150))
    categoria = db.relationship('Tamanho',backref='tamanhos')

    def __repr__(self):
        return f'<{self.id}, {self.nome}>'
        # {self.categoria}

class Tamanho(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150))
    cat_id = db.Column(db.Integer, db.ForeignKey('categoria.id'))

    def __repr__(self):
        return f'<{self.id}, {self.nome}, {self.tamanhos.nome}>'
