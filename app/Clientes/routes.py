from flask import Blueprint, render_template, redirect, url_for, flash
# ***********************************************************************************************
clientes = Blueprint('clientes', __name__, template_folder='pages')
# ***********************************************************************************************
@clientes.route('/', methods=['GET','POST'])
def listar_clientes():
    return render_template('/clientes.html')    