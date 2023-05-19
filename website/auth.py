from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Cliente, Produto
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user
from .forms import FormLogin
# ***********************************************************************************************
auth = Blueprint('auth', __name__)
# ***********************************************************************************************
# ENTRAR - LOGAR
# ***********************************************************************************************
@auth.route('/', methods=['GET', 'POST'])
def login():
    logout_user()
    # ADICIONAR USUARIO ROOT      
    email_ja_existe = User.query.filter_by(email='adm@adm.com.br').first()
    if email_ja_existe == None:    
        root_user = User(email='adm@adm.com.br', first_name='ADMINISTRADOR', password=generate_password_hash(
        '123456', method='sha256')) 
        db.session.add(root_user)
        db.session.commit()
    # ADICIONAR CLIENTE DESCONHECIDO      
    fone_ja_existe = Cliente.query.filter_by(fone='(99) 9-9999-9999').first()
    if fone_ja_existe == None:    
        desconhecido = Cliente(nome='DESCONHECIDO', fone='(99) 9-9999-9999')
        db.session.add(desconhecido)
        db.session.commit()
    # -----------------------------------------------------------------------------------------------  
    # ADICIONAR PRODUTO TESTE
    existe_algum_produto = Produto.query.all()
    if existe_algum_produto == None:
        one = Produto(categoria='ESPETOS', descricao='ESPETO CONTRA-FILE', tamanho='100-G', valor=15, user_id=1)
        db.session.add(one)
        db.session.commit()  

    form=FormLogin()
    if form.validate_on_submit():  
        if request.method == 'POST':
            email = request.form.get('email')
            password = request.form.get('senha')
            
            user = User.query.filter_by(email=email).first()
            if user:
                if check_password_hash(user.password, password):
                    login_user(user, remember=True)
                    return redirect(url_for('views.comandas'))
                else:
                    flash('SENHA INCORRETA !!!', category='error')
            else:
                flash('EMAIL NÃO CADASTRADO !!!', category='error')

    return render_template("entrar.html", form=form, user=current_user)
# ***********************************************************************************************
# SAIR - DESLOGAR
# ***********************************************************************************************
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
# ***********************************************************************************************
# CADASTRAR USUARIOS
# ***********************************************************************************************
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)

            return redirect(url_for('views.comandas'))

    return render_template("sign_up.html", user=current_user)
# ***********************************************************************************************