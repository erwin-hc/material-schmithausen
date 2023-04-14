from flask import Flask, render_template, url_for, redirect, request
import sqlalchemy
from forms import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ÇALDKFJAÇALDKJFALFJ'

@app.route('/', methods=['GET','POST'])
def login():
    form = FormLogin(request.form)
    if request.method == ['POST']:
        return 'FORMULARIO SUBMETIDO COM SUCESSO'
    else:
        return 'ERROR'
    
    return render_template('login.html', form=form)

@app.route('/comandas.html', methods=['GET','POST'])
def comandas():
    return render_template('comandas.html')


if __name__ == '__main__':
    # app.run(host='192.168.0.216',debug=True)
    app.run(host='10.0.0.53',debug=True)