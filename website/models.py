from . import db
import datetime
from flask_login import UserMixin
from sqlalchemy.sql import func
# ---------------------------------------------------------------
# MODELO CLIENTES
# ---------------------------------------------------------------    
class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fone = db.Column(db.String(150))
    data_criacao = db.Column(db.DateTime(timezone=True), default=func.now())
    nome = db.Column(db.String(150))
    comandas = db.relationship('Comanda',backref='comandas')    
# ---------------------------------------------------------------
# MODELO USUARIOS
# ---------------------------------------------------------------
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    user = db.relationship('Produto',backref='produto')    
# ---------------------------------------------------------------
# MODELO PRODUTOS
# ---------------------------------------------------------------    
class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(150))
    valor = db.Column(db.Float)
    data_criacao = db.Column(db.DateTime(timezone=True), default=func.now())

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    cat_id = db.Column(db.Integer, db.ForeignKey('categoria.id'))
    tam_id = db.Column(db.Integer, db.ForeignKey('tamanho.id'))

    usuario = db.relationship('User',backref='usuarios')  
    categoria = db.relationship('Categoria',backref='categorias')  
    tamanho = db.relationship('Tamanho',backref='tamanho')  

# ---------------------------------------------------------------
# MODELO CATEGORIAS
# ---------------------------------------------------------------
class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150))
    categoria = db.relationship('Tamanho',backref='tamanhos')
# ---------------------------------------------------------------
# MODELO TIPOS/TAMANHOS
# ---------------------------------------------------------------
class Tamanho(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150))
    cat_id = db.Column(db.Integer, db.ForeignKey('categoria.id'))
# ---------------------------------------------------------------
# MODELO FLUXO_DIARIO
# ---------------------------------------------------------------
class Fluxo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime(timezone=True), default=func.now())
    status = db.Column(db.String(100))
    total = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    comanda_id = db.Column(db.Integer, db.ForeignKey('comanda.id'))
# ---------------------------------------------------------------
# MODELO COMANDA
# ---------------------------------------------------------------
class Comanda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime(timezone=True), default=func.now())
    numero = db.Column(db.Integer)
    status = db.Column(db.String(100))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    intes_id = db.Column(db.Integer, db.ForeignKey('itens.id'))

    forma_pgto = db.Column(db.String(50))
    total = db.Column(db.Float)
# ---------------------------------------------------------------
# MODELO ITENS_COMANDA
# ---------------------------------------------------------------
class Itens(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime(timezone=True), default=func.now())
    comanda_id = db.Column(db.Integer, db.ForeignKey('comanda.id'))
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'))
    qtd = db.Column(db.Integer)


