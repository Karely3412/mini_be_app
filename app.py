# import psycopg2
from flask import Flask
from flask_marshmallow import Marshmallow
import os
from db import *

from models.users import Users
from models.imessages import Imessages
from routes.user_route import users
from routes.imessage_route import imessages


def register_blueprints(app):
    app.register_blueprint(users)
    app.register_blueprint(imessages)


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

init_db(app, db)

def create_tables():
    with app.app_context():
        print("Creating Tables...")
        db.create_all()
        print("Tables created successfully")

create_tables()
register_blueprints(app)


if __name__ ==  '__main__':
    app.run(host= '0.0.0.0', port='8086', debug=True)

