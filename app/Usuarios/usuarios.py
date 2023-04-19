from flask import Blueprint, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Length, Email

# ***********************************************************************************************
class FormCadastroUsuarios(FlaskForm):
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
usuarios = Blueprint('usuarios', __name__, template_folder='pages')
# ***********************************************************************************************
@usuarios.route('/', methods=['GET','POST'])
def listar_usuarios():
    form = FormCadastroUsuarios()
    return render_template('/usuarios.html', form=form)    