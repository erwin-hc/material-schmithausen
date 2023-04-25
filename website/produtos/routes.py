from flask import Blueprint, render_template

produtos_bp = Blueprint('produtos', __name__, template_folder='pages')

@produtos_bp.route('/produtos',methods=['GET','POST'])
def produtos():
	return render_template('produtos.html')
