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

# CATEGORIAS
    # print(Categoria.query.all())
    # ct1 = Categoria(nome='ESPETOS')
    # ct2 = Categoria(nome='REFRIGERANTES')
    # ct3 = Categoria(nome='CERVEJAS')
    # db.session.add(ct1)
    # db.session.add(ct2)
    # db.session.add(ct3)
    # db.session.commit()

# TAMANHOS ESPETOS
    # print(Tamanho.query.all())
    # e1 = Tamanho(nome='100-G',cat_id=1)
    # e2 = Tamanho(nome='150-G',cat_id=1)
    # e3 = Tamanho(nome='200-G',cat_id=1)
    # db.session.add(e1)
    # db.session.add(e2)
    # db.session.add(e3)
    # db.session.commit()

# TAMANHO REFRIGERANTES
    # print(Tamanho.query.all())
    # r1 = Tamanho(nome='LATA 200-ML',cat_id=2)
    # r2 = Tamanho(nome='LATA 310-ML',cat_id=2)
    # r3 = Tamanho(nome='LATA 350-ML',cat_id=2)
    # r4 = Tamanho(nome='PET 600-ML',cat_id=2)
    # r5 = Tamanho(nome='PET 1,0-LTS',cat_id=2)
    # r6 = Tamanho(nome='PET 1,5-LTS',cat_id=2)
    # r7 = Tamanho(nome='PET 2,0-LTS',cat_id=2)
    # db.session.add(r1)
    # db.session.add(r2)
    # db.session.add(r3)
    # db.session.add(r4)
    # db.session.add(r5)
    # db.session.add(r6)
    # db.session.add(r7)
    # db.session.commit()
# TAMANHO CERVEJAS
    # print(Tamanho.query.all())
    # c1 = Tamanho(nome='LATA 269-ML',cat_id=3)
    # c2 = Tamanho(nome='LATA 275-ML',cat_id=3)
    # c3 = Tamanho(nome='LATA 350-ML',cat_id=3)
    # c4 = Tamanho(nome='LATAO 473-ML',cat_id=3)
    # c5 = Tamanho(nome='GARRAFA 600-ML',cat_id=3)
    # db.session.add(c1)
    # db.session.add(c2)
    # db.session.add(c3)
    # db.session.add(c4)
    # db.session.add(c5)
    # db.session.commit()


    # existis_fone = Cliente.query.filter_by(fone=fone).first()
    return render_template("comandas.html", user=current_user, data=data)

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX 
# USUARIOS   
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  

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
                return redirect(url_for('views.cadastroUsuarios'))
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
            return redirect(url_for('views.usuarios'))
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
    return redirect(url_for('views.usuarios'))
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX 
# CLIENTES   
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
            return redirect(url_for('views.clientes'))    
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
    return redirect(url_for('views.clientes'))
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX 
# PRODUTOS   
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  

# ***********************************************************************************************
#  LISTAR PRODUTOS
# ***********************************************************************************************
@views.route('/produtos', methods=['GET','POST'])
@login_required
def produtos():
    produtos = Produto.query.all()
    # print(Produto.query.all())
    # criador = User.query.filter_by(id=current_user.id).first()
    # myData = db.session.query(Produto)\
    #     .join(User, User.id == Produto.user_id)\
    #         .with_entities(
    #             User.first_name,
    #             Produto.id,
    #             Produto.descricao,
    #             Produto.categoria,
    #             Produto.tamanho,
    #             Produto.valor,
    #             Produto.data_criacao
    #             ).all()

    return render_template("produtos_listar.html", 
        user=current_user,
        data=data, 
        produtos=produtos)
# ***********************************************************************************************
#  CADASTRO PRODUTOS
# ***********************************************************************************************
@views.route('/produtos_cadastrar', methods=['GET','POST'])
@login_required
def cadastroProdutos():
    form = CadastroProduto()
    form.categoria.query = Categoria.query    
    form.tamanho.query = Tamanho.query.filter_by(cat_id=1).all()

    if form.validate_on_submit():
        if request.method == 'POST':
            categoria = request.form.get('categoria')
            tamanho = request.form.get('tamanho')
            descricao = request.form.get('descricao').upper()   
            valor = request.form.get('valor')
            criador = current_user.id
            novo_produto = Produto(categoria=categoria,tamanho=tamanho,descricao=descricao,valor=valor,user_id=criador)
            db.session.add(novo_produto)
            db.session.commit()
            return redirect(url_for('views.produtos'))
        else:
            return render_template('produtos_cadastrar.html',
                user=current_user,
                data=data, 
                form=form)
            
    return render_template('produtos_cadastrar.html',
        user=current_user,
        data=data, 
        form=form)

@views.route('/categoria/<int:id>')
def categoria(id):
    tam = Tamanho.query.filter_by(cat_id=id).all()
    newArray = []
    for row in tam:
        print(row.cat_id)
        obj = {}
        obj['valor'] = row.cat_id
        obj['nome'] = row.nome
        newArray.append(obj)
    print(newArray)
    return newArray
# ***********************************************************************************************
# DELETAR PRODUTO
# ***********************************************************************************************
@views.route('/produtos_deletar/<int:id>', methods=['POST','GET'])
def deletarProduto(id):  
    get_produto = Produto.query.get(id)
    if get_produto:
        db.session.delete(get_produto)
        db.session.commit()
    return redirect(url_for('views.produtos'))

