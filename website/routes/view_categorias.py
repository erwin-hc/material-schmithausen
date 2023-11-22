from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask import get_flashed_messages
from flask_login import login_required, current_user
from .. import db
from ..models import *
# from ..forms.forms_usuarios import *
# from ..forms.forms_clientes import *
# from ..forms.forms_login import *
# from ..forms.forms_produtos import *
import datetime

# ***********************************************************************************************
# DATA ATUAL
# ***********************************************************************************************
data = datetime.datetime.now().date()
# ***********************************************************************************************
view_categorias = Blueprint('view_categorias', __name__)



# ***********************************************************************************************
# CATEGORIAS -- LISTAR
# ***********************************************************************************************
@view_categorias.route('/categorias', methods=['GET','POST'])
@login_required
def categorias():
    get_flashed_messages()
    categorias = Categoria.query.all()
    tamanhos = Tamanho.query.all()

    return render_template("categorias_listar.html", 
        user=current_user,
        data=data, 
        tamanhos=tamanhos,
        categorias=categorias)
# ***********************************************************************************************
# CATEGORIAS -- CADASTRAR
# ***********************************************************************************************
@view_categorias.route('/categorias_cadastrar/<string:nome>', methods=['GET','POST'])
@login_required
def categoriaCadastrar(nome):
    categorias = Categoria.query.all()
    tamanhos = Tamanho.query.all()

    if request.method == 'GET':
        nova_categoria = Categoria(nome=nome.upper())
        db.session.add(nova_categoria)
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
# CATEGORIAS -- DELETAR
# ***********************************************************************************************
@view_categorias.route('/categorias_deletar/<int:id>', methods=['GET','POST'])
@login_required
def categoriaDeletar(id):
    categorias = Categoria.query.all()
    tamanhos = Tamanho.query.all()
    # exixte_em_produtos = Produto.query.filter_by(categoria=id).all()
    exixte_em_produtos = Produto.query.join(Produto.categoria).filter(Categoria.id == id).all()
    get_categorias = Categoria.query.get(id)

    if exixte_em_produtos:
        flash('NÃO PODE SER EXCLUÍDO!!!')
        return redirect(url_for("view_categorias.categorias"))
    else:
        if request.method == 'GET':
            if get_categorias:
                db.session.delete(get_categorias)
                db.session.commit()
                return redirect(url_for('view_categorias.categorias'))
        
    return render_template("categorias_listar.html", 
        user=current_user,
        data=data, 
        categorias=categorias,
        tamanhos=tamanhos)
# ***********************************************************************************************
# CATEGORIAS -- ATUALIZAR
# ***********************************************************************************************
@view_categorias.route('/categorias_atualizar/<int:id>/<string:valor>', methods=['GET','POST'])
@login_required
def categoriaAtualizar(id, valor):
    categorias = Categoria.query.all()
    tamanhos = Tamanho.query.all()
    cat_id = id
    cat_valor = valor

    get_categorias = Categoria.query.get(cat_id)

    if request.method == 'GET':
        if get_categorias:
            get_categorias.nome = cat_valor.upper()
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