from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .. import db
from ..models.models import *
import datetime

# DATA ATUAL
data = datetime.datetime.now().date()
# ***********************************************************************************************
view_comandas = Blueprint('view_comandas', __name__)

# ***********************************************************************************************
# COMANDAS LISTAR
# ***********************************************************************************************
@view_comandas.route('/comandas', methods=['GET', 'POST'])
@login_required
def comandas():
    df_produtos = Produto.query.all()
    return render_template("comandas.html",
                           user=current_user,
                           data=data,
                           dfProdutos = df_produtos)