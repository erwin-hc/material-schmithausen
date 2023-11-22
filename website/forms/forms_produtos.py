from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length
from wtforms_sqlalchemy.fields import QuerySelectField

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