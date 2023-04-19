from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Length, Email
from flask_login import login_required
# ***********************************************************************************************
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
		Length(min=6, message=('Pelo menos 6 caracteres!'))
		])
	enviar = SubmitField('Entrar')
# ***********************************************************************************************