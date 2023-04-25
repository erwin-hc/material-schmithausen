from flask import Flask

def create_app():
	app = Flask(__name__)
	app.config['SECRET_KEY'] = 'mySecretKey'

	from .auth.routes	  import auth_bp
	from .comandas.routes import comandas_bp
	from .produtos.routes import produtos_bp
	from .usuarios.routes import usuarios_bp
	from .clientes.routes import clientes_bp

	app.register_blueprint(auth_bp, url_prefix='/')
	app.register_blueprint(comandas_bp, url_prefix='/')
	app.register_blueprint(produtos_bp, url_prefix='/')
	app.register_blueprint(usuarios_bp, url_prefix='/')
	app.register_blueprint(clientes_bp, url_prefix='/')

	return app