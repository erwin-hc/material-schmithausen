from flask import Blueprint, render_template, redirect, url_for, flash
# ***********************************************************************************************

# ***********************************************************************************************
produtos = Blueprint('produtos', __name__, template_folder='pages')
# ***********************************************************************************************
@produtos.route('/', methods=['GET','POST'])
def listar_produtos():
    return render_template('/produtos.html')    