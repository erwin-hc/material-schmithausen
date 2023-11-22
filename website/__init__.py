from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    db.init_app(app)

    from .routes.view_helpers import view_helpers
    from .routes.view_login import auth
    from .routes.view_comandas import view_comandas
    from .routes.view_usuarios import view_usuarios
    from .routes.view_clientes import view_clientes
    from .routes.view_produtos import view_produtos
    from .routes.view_categorias import view_categorias
    from .routes.view_tamanhos import view_tamanhos
    
    app.register_blueprint(view_helpers, url_prefix='/')
    app.register_blueprint(view_comandas, url_prefix='/')
    app.register_blueprint(view_usuarios, url_prefix='/')
    app.register_blueprint(view_clientes, url_prefix='/')
    app.register_blueprint(view_produtos, url_prefix='/')
    app.register_blueprint(view_categorias, url_prefix='/')
    app.register_blueprint(view_tamanhos, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Cliente, Produto
    
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.login_message = u"FAVOR EFETUAR LOGIN!"

    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')

