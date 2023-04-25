from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, PasswordField
from wtforms.validators import ValidationError, DataRequired, Length, Email, EqualTo
# ************************************************************************************
class FormCadastroUsuarios(FlaskForm):
	usuario = StringField(
		'Usuário',
		validators = [
		DataRequired(message=('Este campo é obrigatório!')),
		Length(min=4, message=('Pelo menos 4 caracteres!'))
		])
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
		Length(min=6, message=('Pelo menos 6 caracteres!')),
		EqualTo('confirmar', message=('As senhas devem ser iguais!'))
		])
	confirmar = PasswordField(
		'Senha (Confirmar)',
		validators = [
		DataRequired(message=('Este campo é obrigatório!')),
		Length(min=6, message=('Pelo menos 6 caracteres!')),
		EqualTo('confirmar', message=('As senhas devem ser iguais!'))
		])
	cadastrar = SubmitField('CADASTRAR')
# ************************************************************************************
usuarios_bp = Blueprint('usuarios', __name__, template_folder='pages')
# ************************************************************************************
@usuarios_bp.route('/usuarios', methods=['GET','POST'])
def cadastrar():
    form = FormCadastroUsuarios()
    if form.validate_on_submit():  
        if form.email.data == 'erwin.stein@gmail.com' and form.senha.data == 'erwinstein':
            return redirect(url_for('comandas.comandas'))
        else: 
            flash('Email e senha não conferem!')
            return render_template('entrar.html',form=form)
    return render_template('usuarios.html', form=form)  
