from flask import Blueprint, render_template

blu_comandas = Blueprint('blu_comandas', __name__, template_folder='pages')

@blu_comandas.route('/comandas')
def comandas():
	return render_template('/comandas.html')