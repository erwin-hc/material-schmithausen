from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import  login_required, current_user
from .. import db
from ..models import *
from ..forms.forms_produtos import *
import datetime

# ***********************************************************************************************
# DATA ATUAL
# ***********************************************************************************************
data = datetime.datetime.now().date()
# ***********************************************************************************************
view_produtos = Blueprint('view_produtos', __name__)

# ***********************************************************************************************
# PRODUTOS -- LISTAR
# ***********************************************************************************************
@view_produtos.route('/produtos', methods=['GET','POST'])
@login_required
def produtos():
    produtos = Produto.query.all()
    tamanhos = Tamanho.query.all()
    categorias = Categoria.query.all()
    return render_template("produtos_listar.html", 
        user=current_user,
        data=data, 
        produtos=produtos,
        tamanhos=tamanhos,
        categorias=categorias)        
# ***********************************************************************************************
# PRODUTOS -- CADASTRAR
# ***********************************************************************************************
@view_produtos.route('/produtos_cadastrar', methods=['POST','GET'])
@login_required
def cadastroProdutos():
    form = CadastroProduto()
    form.categoria.query = Categoria.query 
    form.tamanho.query = Tamanho.query
    espetos =  db.session.query(Tamanho).join(Categoria).filter(Categoria.id == 1).all()
    objTamanhos = Tamanho.query.all()
    catArray = []
    
    for row in objTamanhos:
        obj = {}
        obj['tam_id'] = row.id
        obj['tam_nome'] = row.nome
        obj['cat_id'] = row.tamanhos.id
        obj['cat_nome'] = row.tamanhos.nome
        catArray.append(obj)
    if form.validate_on_submit():
        if request.method == 'POST':
            categoria = request.form.get('categoria')
            tamanho = request.form.get('tamanho')
            descricao = request.form.get('descricao').upper()   
            valor = float(request.form.get('valor').replace(",","."))
            criador = current_user.id
            novo_produto = Produto(cat_id=categoria,tam_id=tamanho,descricao=descricao,valor=valor,user_id=criador)
            db.session.add(novo_produto)
            db.session.commit()
            return redirect(url_for('view_produtos.produtos'))
        else:
            return render_template('produtos_cadastrar.html',
                user=current_user,
                data=data, 
                form=form,
                espetos=espetos,
                objTamanhos=catArray)            
    return render_template('produtos_cadastrar.html',
        user=current_user,
        data=data, 
        form=form,
        espetos=espetos,
        objTamanhos=catArray)
# ***********************************************************************************************
# PRODUTOS -- DELETAR
# ***********************************************************************************************
@view_produtos.route('/produtos_deletar/<int:id>', methods=['POST','GET'])
def deletarProduto(id):  
    get_produto = Produto.query.get(id)
    if get_produto:
        db.session.delete(get_produto)
        db.session.commit()
    return redirect(url_for('view_produtos.produtos'))
# ***********************************************************************************************
# PRODUTOS -- ATUALIZAR
# ***********************************************************************************************
@view_produtos.route('/produtos_atualizar/<int:id>/<int:cat>/<int:tam>', methods=['GET','POST'])
@login_required
def atualizarProdutos(id,cat,tam):
    form = CadastroProduto()
    form.categoria.query = Categoria.query 
    form.tamanho.query = Tamanho.query
    get_pro = Produto.query.get(id)
    
    objTamanhos = Tamanho.query.all()
    catArray = []
    for row in objTamanhos:
        obj = {}
        obj['tam_id'] = row.id
        obj['tam_nome'] = row.nome
        obj['cat_id'] = row.tamanhos.id
        obj['cat_nome'] = row.tamanhos.nome
        catArray.append(obj)
  
    get_cat_text = Categoria.query.get(cat).nome
    get_tam_text = Tamanho.query.get(tam).nome

    if form.validate_on_submit():
        if request.method == 'POST':
            categoria = request.form.get('categoria')
            tamanho = request.form.get('tamanho')
            descricao = request.form.get('descricao').upper()   
            valor = float(request.form.get('valor').replace(",","."))
            criador = current_user.id
            get_pro.cat_id = categoria
            get_pro.tam_id = tamanho
            get_pro.descricao = descricao
            get_pro.valor = valor
            db.session.commit()
            return redirect(url_for('view_produtos.produtos'))


    return render_template('produtos_atualizar.html', 
    user=current_user, 
    data=data, 
    form=form,
    p=get_pro,
    objTamanhos=catArray,
    tamTex=get_tam_text,
    catTex=get_cat_text
    )
