from website import create_app
import yagmail,os
from flask_sqlalchemy import SQLAlchemy
#from website import celery
#from website.celery import make_celery

from datetime import datetime, timedelta
now = datetime.now()
basedir = os.path.abspath(os.path.dirname(__file__))
import yagmail

yag = yagmail.SMTP('testingcelery2021', 'Pyth0nC0d3r.2791')

app,celery = create_app()

# Build the Sqlite ULR for SqlAlchemy
sqlite_url = "sqlite:///" + os.path.join(basedir, "palabras.db")

# Configure the SqlAlchemy part of the app instance
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = sqlite_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Create the SqlAlchemy db instance
db = SQLAlchemy(app)
db.init_app(app)

@celery.task
def send_with_attachment(to, subject, content, attachment):
    yag.send(
        to=to,
        subject=subject,
        contents=content,
        attachments=attachment,
    )


@celery.task
def send_without_attachment(to, subject, content):
    yag.send(
        to=to,
        subject=subject,
        contents=content
    )

@app.route('/mailer', methods=['GET', 'POST'])
def mailer():
    email_to='testingcelery2021@gmail.com'

    send_without_attachment(
    email_to,
    'Celery Testing',
    'Esto es una envio desde flask con Celery'
    )
    
    return (f'Email has been Sent to: {email_to}')

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0')
    
