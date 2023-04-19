from flask import Flask 
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from app.Comandas.comandas import comandas
from app.Login.login import login
from app.Usuarios.usuarios import usuarios
from app.Clientes.clientes import clientes
from app.Produtos.produtos import produtos
from app.Fluxo.fluxo import fluxo

app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schmithausen.sqlite3'
app.config['SECRET_KEY'] = 'ÇALDKFJAÇALDKJFALFJ'
db = SQLAlchemy(app)

app.register_blueprint(login, url_prefix='/')
app.register_blueprint(comandas, url_prefix='/comandas')
app.register_blueprint(usuarios, url_prefix='/usuarios')
app.register_blueprint(clientes, url_prefix='/clientes')
app.register_blueprint(produtos, url_prefix='/produtos')
app.register_blueprint(fluxo, url_prefix='/fluxo')


if __name__ == '__main__':
    # app.run(host='192.168.0.216',debug=True)
    app.run(host='10.0.0.53',debug=True)