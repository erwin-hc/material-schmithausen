from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from .models import User
from . import db
import json
import datetime
# ***********************************************************************************************
# DATA ATUAL
# ***********************************************************************************************
data = x = datetime.datetime.now().date()
# ***********************************************************************************************

views = Blueprint('views', __name__)
# ***********************************************************************************************
# COMANDAS
# ***********************************************************************************************
@views.route('/comandas', methods=['GET', 'POST'])
@login_required
def comandas():
    return render_template("comandas.html", user=current_user, data=data)
# ***********************************************************************************************
# DELETE NOTE
# ***********************************************************************************************
@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})
# ***********************************************************************************************
#  USUARIOS
# ***********************************************************************************************
@views.route('/usuarios', methods=['GET','POST'])
@login_required
def usuarios():
    users = []
    rows = User.query.all()
    for r in rows:
        users.append(r)
        
    return render_template("usuarios.html", user=current_user, data=data, users=users)