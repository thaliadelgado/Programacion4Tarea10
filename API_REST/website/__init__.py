import celery
from flask import Flask
import redis
from website.celery import make_celery

def create_app():
    flask_app = Flask(__name__)
    flask_app.config.update(
    CELERY_BROKER_URL='amqp://localhost//',
    CELERY_IMPORTS=("send_email", "app", "<other-filenames-that-want-access>")
)
    # make redis
    redis_cache = redis.StrictRedis()
    celery = make_celery(flask_app)

# make flask app
    #app = Flask(__name__)
    from .views import views
    from .auth import auth

    flask_app.register_blueprint(views, url_prefix='/')
    flask_app.register_blueprint(auth, url_prefix='/')

    
    return flask_app,celery

    

