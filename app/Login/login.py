from flask import Blueprint, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Length, Email

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
blu_login = Blueprint('blu_login', __name__, template_folder='pages')
# ***********************************************************************************************
@blu_login.route('/', methods=['GET','POST'])
def login():
    form = FormLogin()
    if form.validate_on_submit():  
        if form.email.data == 'erwin.stein@gmail.com' and form.senha.data == 'erwinstein':
            # return render_template('/comandas.html')
            return redirect(url_for('blu_comandas.comandas'))
        else: 
            flash('Email e senha não conferem!')
            return redirect(url_for('blu_login.login'))
            # return render_template('/login.html')
    
    return render_template('/login.html', form=form)    