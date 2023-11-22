from flask import Blueprint, render_template, request, redirect,session
from flask_login import login_required, current_user
from .. import db
from ..models import *
import datetime

# ***********************************************************************************************
# DATA ATUAL
# ***********************************************************************************************
data = datetime.datetime.now().date()
# ***********************************************************************************************
view_helpers = Blueprint('view_helpers', __name__)

# ***********************************************************************************************
# TOOGLE-THEME
# ***********************************************************************************************
@view_helpers.route("/toggle-theme")
def toggle_theme():
    current_theme = session.get("theme")
    if current_theme == "light":
        session["theme"] = "dark"
    else:
        session["theme"] = "light"

    return redirect(request.args.get("current_page"))

# ***********************************************************************************************
# FILTRO PRODUTOS - CATEGORIAS
# ***********************************************************************************************
@view_helpers.route('/filtro_produtos/<int:id>', methods=['GET','POST'])
@login_required
def filtroprodutos(id):
    # produtos = Produto.query.all()
    get_categoria = Categoria.query.get(id)
    tamanhos = Tamanho.query.all()
    categorias = Categoria.query.all()
    id=id

    if get_categoria:
        produtos = Produto.query.filter_by(cat_id=id).all()
    else:    
        produtos = Produto.query.all()

    return render_template("produtos_listar.html", 
        id=id,
        user=current_user,
        data=data, 
        produtos=produtos,
        tamanhos=tamanhos,
        categorias=categorias)  




