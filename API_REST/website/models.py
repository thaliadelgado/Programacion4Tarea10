from datetime import datetime
from website.db import db, BaseModelMixin

class Palabra(db.Model, BaseModelMixin):
    __tablename__ = 'palabras'
    id = db.Column(db.Integer, primary_key=True)
    palabra = db.Column(db.String(32), index=True)
    significado = db.Column(db.String(32))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

