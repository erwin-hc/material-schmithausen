from flask_wtf import FlaskForm
from wtforms import StringField, EmailField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms.widgets import PasswordInput

class CadastroUsuario(FlaskForm):
	nome = StringField(
		'Nome',
		validators= [
		DataRequired(message=("Este campo é obrigatório!")),
		Length(min=4, message=("Pelo menos 4 caracteres!"))
		])
	email = EmailField(
		'Email',
		validators = [
		DataRequired(message=('Este campo é obrigatório!')),
		Email(message=('Digite um email válido!')),
		])
	senha = StringField(
		'Senha',
		widget=PasswordInput(hide_value=False),
		validators = [
		DataRequired(message=('Este campo é obrigatório!')),
		Length(min=6, message=('Pelo menos 6 caracteres!')),
		EqualTo('confirmar', message=("Senhas não conferem!"))
		])
	confirmar = StringField(
		'Senha (Confirmar)',
		widget=PasswordInput(hide_value=False),
		validators = [
		DataRequired(message=('Este campo é obrigatório!')),
		Length(min=6, message=('Pelo menos 6 caracteres!'))
		])

