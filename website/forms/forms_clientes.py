from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, PasswordField, SelectField, FloatField
from wtforms.validators import ValidationError, DataRequired, Length, Email, EqualTo
from wtforms.widgets import PasswordInput, Select
from wtforms_sqlalchemy.fields import QuerySelectField

class CadastroCliente(FlaskForm):
	nome = StringField(
	'Nome',
	validators= [
	DataRequired(message=("Este campo é obrigatório!")),
	Length(min=4, message=("Pelo menos 4 caracteres!"))
	])
	fone = StringField(
	'Celuar',
	validators= [
	DataRequired(message=("Este campo é obrigatório!")),
	Length(min=16,max=16, message=("Número celuar inválido!"))
	])