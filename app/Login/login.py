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
login = Blueprint('login', __name__, template_folder='pages')
# ***********************************************************************************************
@login.route('/', methods=['GET','POST'])
def listar_login():
    form = FormLogin()
    if form.validate_on_submit():  
        if form.email.data == 'erwin.stein@gmail.com' and form.senha.data == 'erwinstein':
            # return render_template('/comandas.html')
            return redirect(url_for('comandas.listar_comandas'))
        else: 
            flash('Email e senha não conferem!')
            return redirect(url_for('login.listar_login'))
            # return render_template('/login.html')
    
    return render_template('/login.html', form=form)    