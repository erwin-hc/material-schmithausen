from flask import Blueprint, render_template

comandas_bp = Blueprint('comandas', __name__, template_folder='pages')
@comandas_bp.route('/comandas',methods=['POST','GET'])
def comandas():
	return render_template('/comandas.html')