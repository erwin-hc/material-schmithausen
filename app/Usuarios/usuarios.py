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
blu_usuarios = Blueprint('blu_usuarios', __name__, template_folder='pages')
# ***********************************************************************************************
@blu_usuarios.route('/usuarios.html', methods=['GET','POST'])
def usuarios():
    form = FormCadastroUsuarios()
    return render_template('/usuarios.html', form=form)    