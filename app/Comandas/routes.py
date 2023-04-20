from flask import Blueprint, render_template

comandas = Blueprint('comandas', __name__, template_folder='pages')

@comandas.route('/')
def listar_comandas():
	return render_template('/comandas.html')