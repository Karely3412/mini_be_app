import psycopg2
import os
from flask import Flask
from flask_marshmallow import Marshmallow
from db import *


app = Flask(__name__)


if __name__ ==  '__main__':
    app.run(host= '0.0.0.0', port='8086')