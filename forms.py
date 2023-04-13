from wtforms import Form, StringField, EmailField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import  ValidationError, Email, InputRequired, Length

class FormLogin(Form):
	email = EmailField(
		'Email',
		validators = [
		InputRequired(message=('Preencher este campo!')),
		Email(message=('Digite um email válido!')),
		])
	senha = StringField(
		'Senha',
		validators = [
		InputRequired(message=('Preencher este campo!')),
		Length(min=6,max=20, message=('Mínimo 6 caracteres!'))
		])

	enviar = SubmitField('Entrar')