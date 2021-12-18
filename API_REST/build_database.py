import os
from config import db
from website.models import Palabra

# Data to initialize database with
PALABRAS = [
    {'palabra': 'MCU', 'significado': 'Marvel Cinematic Universe'}
]

# Delete database file if it exists currently
if os.path.exists('palabras.db'):
    os.remove('palabras.db')

# Create the database
db.create_all()



db.session.commit()