import psycopg2
from flask import Flask
from flask_marshmallow import Marshmallow
import os
from db import *

from models.imessages import Imessages
from models.users import Users


app = Flask(__name__)

app.congfig['DATABASE_URI'] = os.getenv("DATABASE_URI")
app.config["SQLALCHEY_TRACK_MODIFICATIONS"] = False



if __name__ ==  '__main__':
    app.run(host= '0.0.0.0', port='8086')

# left of on 7.2 curr