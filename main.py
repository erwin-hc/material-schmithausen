from flask import Flask, Blueprint
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# *****************************************************************************
from app.Login.routes    import login
from app.Comandas.routes import comandas
from app.Fluxo.routes    import fluxo
from app.Produtos.routes import produtos
from app.Usuarios.routes import usuarios
from app.Clientes.routes import clientes
# *****************************************************************************

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schmithausen.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'ÇALDKFJAÇALDKJFALFJ'

database = SQLAlchemy(app)

app.register_blueprint(login, url_prefix='/')
app.register_blueprint(comandas, url_prefix='/comandas')
app.register_blueprint(usuarios, url_prefix='/usuarios')
app.register_blueprint(clientes, url_prefix='/clientes')
app.register_blueprint(produtos, url_prefix='/produtos')
app.register_blueprint(fluxo, url_prefix='/fluxo')

# login_manager = LoginManager(app)

app.app_context().push()

if __name__ == '__main__':
    app.run(host='192.168.0.216',debug=True)
    # app.run(host='10.0.0.53',debug=True)