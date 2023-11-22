from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .. import db
from ..models import *
from ..forms.forms_clientes import *

import datetime
# ***********************************************************************************************
# DATA ATUAL
# ***********************************************************************************************
data = datetime.datetime.now().date()
# ***********************************************************************************************
view_clientes = Blueprint('view_clientes', __name__)

@view_clientes.route('/clientes', methods=['GET','POST'])
@login_required
def clientes():
    clientes = []
    rows = Cliente.query.all()
    for r in rows:
        clientes.append(r)        
    return render_template("clientes_listar.html", user=current_user, data=data, clientes=clientes)
# ***********************************************************************************************
# CLIENTES -- CADASTRAR
# ***********************************************************************************************
@view_clientes.route('/clientes_cadastrar', methods=['GET','POST'])
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
                return redirect(url_for('view_clientes.clientes'))
    return render_template("clientes_cadastrar.html", user=current_user, data=data, form=form)
# ***********************************************************************************************
# CLIENTES -- DELETAR
# ***********************************************************************************************
@view_clientes.route('/clientes_deletar/<int:id>', methods=['POST', 'GET'])
@login_required
def deletarCliente(id):
    get_cli = Cliente.query.get(id)
    if id == 1:
        flash('NÃO PODE SER EXCLUÍDO!',category='error')
    else:
        if get_cli:
            db.session.delete(get_cli)
            db.session.commit()
            return redirect(url_for('view_clientes.clientes'))
    return redirect(url_for('view_clientes.clientes'))
# ***********************************************************************************************
# CLIENTES -- ATUALIZAR
# ***********************************************************************************************
@view_clientes.route('/clientes_atualizar/<int:id>', methods=['GET','POST'])
@login_required
def atualizarClientes(id): 
    form = CadastroCliente()
    get_cli = Cliente.query.get(id)
    if request.method == 'GET':
        if id != 1:
            return render_template('clientes_atualizar.html', 
                user=current_user, 
                data=data, 
                form=form,
                c=get_cli
                )
        else:
            flash('NÃO PODE SER EDITADO!')
            return redirect(url_for('view_clientes.clientes'))    
    if form.validate_on_submit():
        if request.method == 'POST':
            nome = request.form.get('nome').upper()
            fone = request.form.get('fone')
            existis_fone = Cliente.query.filter_by(fone=fone).first()
            if existis_fone == None or existis_fone.id == id:
                get_cli.nome = nome
                get_cli.fone = fone
                db.session.commit()
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
    return redirect(url_for('view_clientes.clientes'))