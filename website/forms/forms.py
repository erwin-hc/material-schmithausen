from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, PasswordField, SelectField, FloatField
from wtforms.validators import ValidationError, DataRequired, Length, Email, EqualTo
from wtforms.widgets import PasswordInput, Select
from wtforms_sqlalchemy.fields import QuerySelectField
# ***********************************************************************************************
# LOGIN
# ***********************************************************************************************
class FormLogin(FlaskForm):
	email = EmailField(
		'Email',
		validators = [
		DataRequired(message=('Este campo é obrigatório!')),
		Email(message=('Digite um email válido!')),
		])
	senha = PasswordField(
		'Senha',
		validators = [
		DataRequired(message=('Este campo é obrigatório!')),
		Length(min=6, message=('Pelo menos 6 caracteres!'))
		])

# ***********************************************************************************************
# CADASTRO USUARIOS
# ***********************************************************************************************
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

# ***********************************************************************************************
# CADASTRO CLIENTES
# ***********************************************************************************************
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

# ***********************************************************************************************
# CADASTRO PRODUTOS
# ***********************************************************************************************
   
class CadastroProduto(FlaskForm):
	categoria = QuerySelectField(
	get_label='nome',
	allow_blank=True,
	blank_text='-- SELECIONE --',
	validators = [
	DataRequired(message=("Obrigatório!"))
	])

	tamanho = QuerySelectField(
	get_label='nome',
	allow_blank=True,
	blank_text='-- SELECIONE --',
	validators = [
	DataRequired(message=("Obrigatório!"))
	])	

	descricao = StringField('descricao',	
	validators = [
	DataRequired(message=("Obrigatório!")),
	Length(min=4, message=("Pelo menos 4 caracteres!"))
	])

	valor = StringField(
	'valor',
	validators = [
	DataRequired(message=("Obrigatório!"))
	])

