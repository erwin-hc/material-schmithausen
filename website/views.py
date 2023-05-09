from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from . import db
from .models import *
from .forms import *
import datetime
import json

# ***********************************************************************************************
# DATA ATUAL
# ***********************************************************************************************
data = x = datetime.datetime.now().date()
# ***********************************************************************************************

views = Blueprint('views', __name__)
# ***********************************************************************************************
# COMANDAS
# ***********************************************************************************************
@views.route('/comandas', methods=['GET', 'POST'])
@login_required
def comandas():
    return render_template("comandas.html", user=current_user, data=data)
# ***********************************************************************************************
# DELETE NOTE
# ***********************************************************************************************
@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})
# ***********************************************************************************************
#  LISTAR USUARIOS
# ***********************************************************************************************
@views.route('/usuarios', methods=['GET','POST'])
@login_required
def usuarios():
    users = []
    rows = User.query.all()
    for r in rows:
        users.append(r)        
    return render_template("usuarios_listar.html", user=current_user, data=data, users=users)
# ***********************************************************************************************
#  CADASTRO USUARIOS
# ***********************************************************************************************
@views.route('/usuarios_cadastrar', methods=['GET','POST'])
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
            else:
                new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user, remember=True)

            return redirect(url_for('views.usuarios'))

    return render_template("usuarios_cadastrar.html", user=current_user, data=data, form=form)
# ***********************************************************************************************
# DELETAR USUARIO
# ***********************************************************************************************
@views.route('/usuarios_deletar/<int:id>', methods=['POST','GET'])
def deletarUsuario(id):  
    get_users = User.query.get(id)
    if id == 1:
        flash('NÃO PODE SER EXCLUÍDO!',category='error')
    else:
        if get_users:
            db.session.delete(get_users)
            db.session.commit()
            return redirect(url_for('views.usuarios'))

    return redirect(url_for('views.usuarios'))
# ***********************************************************************************************
# ATUALIZAR USUARIOS
# ***********************************************************************************************
@views.route('/usuarios_atualizar/<int:id>', methods=['GET','POST'])
@login_required
def atualizarUsuarios(id): 
    form = CadastroUsuario()
    get_users = User.query.get(id)

    if id != 1:
        if request.method == 'GET': 
            return render_template('usuarios_atualizar.html', 
                user=current_user, 
                data=data, 
                form=form,
                u=get_users
                )

        if request.method == 'POST':
            if form.validate_on_submit():
                nome = request.form.get('nome').upper()
                email = request.form.get('email')
                existis_email = Cliente.query.filter_by(email=email).first()

                if existis_email == None:
                    get_users.nome = nome
                    get_users.email = email
                    db.session.commit()
                    return redirect(url_for('views.usuarios'))
                else:
                    if existis_email.id == id:
                        get_users.nome = nome
                        get_users.fone = fone
                        db.session.commit()
                        return redirect(url_for('views.usuarios'))
                    else:    
                        flash('EMAIL JÁ CADASTRADO !!!', category='error')
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

        return redirect(url_for('views.usuarios'))
    else:
        flash('NÃO PODE SER EDITADO!')
        return redirect(url_for('views.usuarios'))

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    
# ***********************************************************************************************
#  LISTAR CLIENTES
# ***********************************************************************************************
@views.route('/clientes', methods=['GET','POST'])
@login_required
def clientes():
    clientes = []
    rows = Cliente.query.all()
    for r in rows:
        clientes.append(r)        
    return render_template("clientes_listar.html", user=current_user, data=data, clientes=clientes)
# ***********************************************************************************************
#  CADASTRO CLIENTES
# ***********************************************************************************************
@views.route('/clientes_cadastrar', methods=['GET','POST'])
@login_required
def cadastroClientes():
    form = CadastroCliente()
    if form.validate_on_submit():
        if request.method == 'POST':
            nome = request.form.get('nome').upper()
            fone = request.form.get('fone')

            existis_fone = Cliente.query.filter_by(fone=fone).first()
            if existis_fone:
                flash('CELULAR JÁ CADASTRADO !!!', category='error')
            else:
                novo_cliente = Cliente(nome=nome, fone=fone)
                db.session.add(novo_cliente)
                db.session.commit()    

                return redirect(url_for('views.clientes'))

    return render_template("clientes_cadastrar.html", user=current_user, data=data, form=form)
# ***********************************************************************************************
# DELETAR CLIENTES
# ***********************************************************************************************
@views.route('/clientes_deletar/<int:id>', methods=['POST', 'GET'])
@login_required
def deletarCliente(id):
    get_cli = Cliente.query.get(id)
    if id == 1:
        flash('NÃO PODE SER EXCLUÍDO!',category='error')
    else:
        print(get_cli)
        if get_cli:
            db.session.delete(get_cli)
            db.session.commit()
            return redirect(url_for('views.clientes'))

    return redirect(url_for('views.clientes'))

# ***********************************************************************************************
# ATUALIZAR CLIENTES
# ***********************************************************************************************
@views.route('/clientes_atualizar/<int:id>', methods=['GET','POST'])
@login_required
def atualizarClientes(id): 
    form = CadastroCliente()
    get_cli = Cliente.query.get(id)

    if id != 1:
        if request.method == 'GET': 
            return render_template('clientes_atualizar.html', 
                user=current_user, 
                data=data, 
                form=form,
                c=get_cli
                )

        if request.method == 'POST':
            if form.validate_on_submit():
                nome = request.form.get('nome').upper()
                fone = request.form.get('fone')
                existis_fone = Cliente.query.filter_by(fone=fone).first()

                if existis_fone == None:
                    get_cli.nome = nome
                    get_cli.fone = fone
                    db.session.commit()
                    return redirect(url_for('views.clientes'))
                else:
                    if existis_fone.id == id:
                        get_cli.nome = nome
                        get_cli.fone = fone
                        db.session.commit()
                        return redirect(url_for('views.clientes'))
                    else:    
                        flash('CELULAR JÁ CADASTRADO !!!', category='error')
                        return render_template('clientes_atualizar.html', 
                            user=current_user, 
                            data=data, 
                            form=form,
                            c=get_cli
                            )
            else:
                return render_template('clientes_atualizar.html', 
                    user=current_user, 
                    data=data, 
                    form=form,
                    c=get_cli
                    )

        return redirect(url_for('views.clientes'))
    else:
        flash('NÃO PODE SER EDITADO!')
        return redirect(url_for('views.clientes'))
