from flask import Blueprint, render_template, redirect, url_for, flash
# ***********************************************************************************************

# ***********************************************************************************************
fluxo = Blueprint('fluxo', __name__, template_folder='pages')
# ***********************************************************************************************
@fluxo.route('/', methods=['GET','POST'])
def listar_fluxo():
    return render_template('/fluxo.html')    