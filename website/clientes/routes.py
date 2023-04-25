from flask import Blueprint, render_template

clientes_bp = Blueprint('clientes', __name__, template_folder='pages')

@clientes_bp.route('/clientes',methods=['GET','POST'])
def clientes():
	return render_template('clientes.html')