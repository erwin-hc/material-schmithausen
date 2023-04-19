from flask import Blueprint, render_template, redirect, url_for, flash
# ***********************************************************************************************

# ***********************************************************************************************
blu_fluxo = Blueprint('blu_fluxo', __name__, template_folder='pages')
# ***********************************************************************************************
@blu_fluxo.route('/fluxo.html', methods=['GET','POST'])
def fluxo():
    return render_template('/fluxo.html')    