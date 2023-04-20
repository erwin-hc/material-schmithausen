from main import database as db
from sqlalchemy import func
from datetime import date
from datetime import datetime

hora_atual = datetime.now().strftime('%H:%M:%S')
data_atual = date.today().strftime('%d-%m-%Y')

class Usuarios(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String)
	email = db.Column(db.String)
	data =  db.Column(db.Date, default=datetime.utcnow)
	hora = db.Column(db.String)

	def __repr__(self):
		return f' {self.id}-{self.nome} | {self.email} | {self.data.strftime("%d-%m-%Y")} | {self.hora} '
db.create_all()

adm = Usuarios(nome='ADMINISTRADOR',email='adm@adm.com',data=date.today(),hora=hora_atual)
erwin = Usuarios(nome='ERWIN GUILHERME STEIN',email='erwin.stein@gmail.com',data=date.today(),hora=hora_atual)


# db.session.add(adm)
# db.session.add(erwin)
# db.session.commit()

for row in (Usuarios.query.all()):
    print(row)