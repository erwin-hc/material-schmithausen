from flask import Blueprint, render_template
# ***********************************************************************************************
# ***********************************************************************************************
usuarios = Blueprint('usuarios', __name__, template_folder='pages')
# ***********************************************************************************************
@usuarios.route('/', methods=['GET','POST'])
def listar_usuarios():
    return render_template('/usuarios.html')    


from main import database
import main

