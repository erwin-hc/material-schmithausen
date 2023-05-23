from .models import *
from . import db   ##means from __init__.py import db

print(categoria.query.all())