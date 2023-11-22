from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash
from flask_login import login_user, login_required, current_user
from .. import db
from ..models import *
from ..forms.forms_usuarios import *
import datetime

# ***********************************************************************************************
# DATA ATUAL
# ***********************************************************************************************
data = datetime.datetime.now().date()
# ***********************************************************************************************
view_usuarios = Blueprint('view_usuarios', __name__)


# ***********************************************************************************************
# USUARIOS -- LISTAR
# ***********************************************************************************************
@view_usuarios.route('/usuarios', methods=['GET','POST'])
@login_required
def usuarios():
    users = []
    rows = User.query.all()
    for r in rows:
        users.append(r)   
    return render_template("usuarios_listar.html", user=current_user, data=data, users=users)
# ***********************************************************************************************
# USUARIOS -- CADASTRAR
# ***********************************************************************************************
@view_usuarios.route('/usuarios_cadastrar', methods=['GET','POST'])
@login_required
def cadastroUsuarios():
    form = CadastroUsuario()
    if form.validate_on_submit():
        if request.method == 'POST':
            email = request.form.get('email')
            first_name = request.form.get('nome')
            password1 = request.form.get('senha')
            password2 = request.form.get('confirmar')
            user = User.query.filter_by(email=email).first()
            if user:
                flash('EMAIL JÁ CADASTRADO!', category='error')
                return redirect(url_for('view_usuarios.cadastroUsuarios'))
            else:
                new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user, remember=True)
            return redirect(url_for('view_usuarios.usuarios'))
    return render_template("usuarios_cadastrar.html", user=current_user, data=data, form=form)
# ***********************************************************************************************
# USUARIOS -- DELETAR
# ***********************************************************************************************
@view_usuarios.route('/usuarios_deletar/<int:id>', methods=['POST','GET'])
def deletarUsuario(id):  
    get_users = User.query.get(id)
    if id == 1:
        flash('NÃO PODE SER EXCLUÍDO!',category='error')
    else:
        if get_users:
            db.session.delete(get_users)
            db.session.commit()
            return redirect(url_for('view_usuarios.usuarios'))
    return redirect(url_for('view_usuarios.usuarios'))
# ***********************************************************************************************
# USUARIOS -- ATUALIZAR
# ***********************************************************************************************
@view_usuarios.route('/usuarios_atualizar/<int:id>', methods=['GET','POST'])
@login_required
def atualizarUsuarios(id): 
    form = CadastroUsuario()
    get_users = User.query.get(id)
    if request.method == 'GET':        
        if id != 1:
            return render_template('usuarios_atualizar.html', 
                user=current_user, 
                data=data, 
                form=form,
                u=get_users
                )
        else:
            flash('NÃO PODE SER EDITADO!')
            return redirect(url_for('view_usuarios.usuarios'))
    if form.validate_on_submit():        
        if request.method == 'POST':
            email = request.form.get('email')
            email_ja_existe = User.query.filter_by(email=email).first()
            if email_ja_existe == None or email_ja_existe.id == id:
                nome = request.form.get('nome')
                email = request.form.get('email')
                get_users.first_name = nome
                get_users.email = email 
                db.session.commit()
            else:
                flash('EMAIL JÁ CADASTRADO!', category='error')
                return render_template('usuarios_atualizar.html', 
                    user=current_user, 
                    data=data, 
                    form=form,
                    u=get_users
                    )   
    else:    
        return render_template('usuarios_atualizar.html', 
                user=current_user, 
                data=data, 
                form=form,
                u=get_users
                ) 
    return redirect(url_for('view_usuarios.usuarios'))