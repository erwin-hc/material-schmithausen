from wtforms import Form, StringField

class FormLogin(Form):
	usuario = StringField('Usuário') 