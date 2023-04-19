from main import db

class Usuarios(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String(150), nullable=False)
	email = db.Column(db.String(150), nullable=False, unique=True)