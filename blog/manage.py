import redis
from flask import Flask
from flask_script import Manager

from back.models import db
from back.views import back_blue
from web.views import web_blue

app = Flask(__name__)
app.register_blueprint(blueprint=back_blue, url_prefix='/back')
app.register_blueprint(blueprint=web_blue, url_prefix='/web')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/blog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1', port=6379)

app.secret_key = '122344hjghfhfdfgdsfsfs'

db.init_app(app)

manage = Manager(app)

if __name__ == '__main__':
    manage.run()
