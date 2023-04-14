from flask_wtf import FlaskForm
from wtforms import StringField, EmailField
from wtforms.validators import DataRequired, Length, Email

class FormLogin(FlaskForm):
	email = EmailField(
		'Email',
		validators = [
		DataRequired(message=('Este campo é obrigatório!')),
		Email(message=('Digite um email válido!')),
		])
	senha = StringField(
		'Senha',
		validators = [
		DataRequired(message=('Este campo é obrigatório!')),
		Length(min=6, message=('Este campo deve ter pelo menos 6 caracteres!'))
		])