from flask import Flask 
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from app.Comandas.comandas import blu_comandas
from app.Login.login import blu_login
from app.Usuarios.usuarios import blu_usuarios
from app.Clientes.clientes import blu_clientes
from app.Produtos.produtos import blu_produtos
from app.Fluxo.fluxo import blu_fluxo

app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schmithausen.sqlite3'
app.config['SECRET_KEY'] = 'ÇALDKFJAÇALDKJFALFJ'
db = SQLAlchemy(app)

app.register_blueprint(blu_login)
app.register_blueprint(blu_comandas)
app.register_blueprint(blu_usuarios)
app.register_blueprint(blu_clientes)
app.register_blueprint(blu_produtos)
app.register_blueprint(blu_fluxo)


if __name__ == '__main__':
    app.run(host='192.168.0.216',debug=True)
    # app.run(host='10.0.0.53',debug=True)