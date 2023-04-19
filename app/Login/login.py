from flask import Blueprint, render_template, redirect, url_for, flash
# ***********************************************************************************************
import sys
sys.path.append("..")
sys.path.append(".")
import app
# ***********************************************************************************************
from forms.forms import FormLogin
# ***********************************************************************************************
login = Blueprint('login', __name__, template_folder='pages')
# ***********************************************************************************************
@login.route('/', methods=['GET','POST'])
def listar_login():
    form = FormLogin()
    if form.validate_on_submit():  
        if form.email.data == 'erwin.stein@gmail.com' and form.senha.data == 'erwinstein':
        	return redirect(url_for('comandas.listar_comandas'))
        else: 
            flash('Email e senha não conferem!')
            return redirect(url_for('login.listar_login'))
    return render_template('/login.html', form=form)    