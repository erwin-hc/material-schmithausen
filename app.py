from flask import Flask 
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from login.login import login
from comandas.comandas import blu_comandas
from login.login import blu_login


app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schmithausen.sqlite3'
app.config['SECRET_KEY'] = 'ÇALDKFJAÇALDKJFALFJ'
db = SQLAlchemy(app)

app.register_blueprint(blu_login)
app.register_blueprint(blu_comandas)


if __name__ == '__main__':
    # app.run(host='192.168.0.216',debug=True)
    app.run(host='10.0.0.53',debug=True)