from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .. import db
from ..models.models import *
import datetime

# ***********************************************************************************************
# DATA ATUAL
# ***********************************************************************************************
data = datetime.datetime.now().date()
# ***********************************************************************************************
view_tamanhos = Blueprint('view_tamanhos', __name__)

# ***********************************************************************************************
# TAMANHOS -- CADASTRAR
# ***********************************************************************************************
@view_tamanhos.route('/tamanos_cadastrar/<int:catId>/<string:nome>', methods=['GET','POST'])
@login_required
def tamanhosCadastrar(catId, nome):
    categorias = Categoria.query.all()
    tamanhos = Tamanho.query.all()

    if request.method == 'GET':
        novo_tamanho = Tamanho(cat_id=catId, nome=nome.upper())
        db.session.add(novo_tamanho)
        db.session.commit() 
        return render_template("categorias_listar.html", 
            user=current_user,
            data=data, 
            categorias=categorias,
            tamanhos=tamanhos)

    return render_template("categorias_listar.html", 
        user=current_user,
        data=data, 
        categorias=categorias,
        tamanhos=tamanhos)
# ***********************************************************************************************
# TAMANHOS -- DELETAR
# ***********************************************************************************************
@view_tamanhos.route('/tamanhos_deletar/<int:id>', methods=['GET','POST'])
@login_required
def tamanhoDeletar(id):
    categorias = Categoria.query.all()
    tamanhos = Tamanho.query.all()
    get_tamanho = Tamanho.query.get(id)
    exixte_em_produtos = Produto.query.join(Produto.tamanho).filter(Tamanho.id == id).all()
    produtos = Produto.query.all()
    

    if exixte_em_produtos:
        flash('NÃO PODE SER EXCLUÍDO!!!')
        return redirect(url_for("view_tamanhos.categorias"))
    else:        
        if get_tamanho:   
            db.session.delete(get_tamanho)
            db.session.commit()
            return redirect(url_for("view_tamanhos.categorias"))
  
    return render_template("categorias_listar.html", 
        user=current_user,
        data=data, 
        categorias=categorias,
        tamanhos=tamanhos)



# ***********************************************************************************************
# TAMANHOS -- ATUALIZAR
# ***********************************************************************************************
@view_tamanhos.route('/tamanhos_atualizar/<int:id>/<string:valor>', methods=['GET','POST'])
@login_required
def tamanhosAtualizar(id, valor):
    categorias = Categoria.query.all()
    tamanhos = Tamanho.query.all()
    tam_id = id
    tam_valor = valor

    get_tamanhos = Tamanho.query.get(tam_id)

    if request.method == 'GET':
        if get_tamanhos:
            get_tamanhos.nome = tam_valor.upper()
            db.session.commit()
            return render_template("categorias_listar.html", 
                user=current_user,
                data=data, 
                categorias=categorias,
                tamanhos=tamanhos)
        
    return render_template("categorias_listar.html", 
        user=current_user,
        data=data, 
        categorias=categorias,
        tamanhos=tamanhos)
