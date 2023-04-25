from flask import Blueprint, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, PasswordField
from wtforms.validators import ValidationError, DataRequired, Length, Email
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
	enviar = SubmitField('Entrar')
# ***********************************************************************************************
auth_bp = Blueprint('auth', __name__, template_folder='pages')
@auth_bp.route('/', methods=['POST','GET'])
@auth_bp.route('/entrar', methods=['POST','GET'])
def entrar():
    form = FormLogin()
    if form.validate_on_submit():  
        if form.email.data == 'erwin.stein@gmail.com' and form.senha.data == 'erwinstein':
            return redirect(url_for('comandas.comandas'))
        else: 
            flash('Email e senha não conferem!')
            return render_template('entrar.html',form=form)
    return render_template('entrar.html', form=form)  
# ************************************************************************************
@auth_bp.route('/sair')
def sair():
	return render_template('sair.html')	
# ************************************************************************************
