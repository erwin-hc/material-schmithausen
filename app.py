from flask import Flask, render_template
import sqlalchemy
from forms import *

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def login():
	return render_template('login.html', form=FormLogin())


if __name__ == '__main__':
    app.run(host='10.0.0.53', debug=True)