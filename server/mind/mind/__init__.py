from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)

app.debug = True


import config

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = config.USER
app.config['MYSQL_DATABASE_PASSWORD'] = config.PASSWORD
app.config['MYSQL_DATABASE_DB'] = config.DB
app.config['MYSQL_DATABASE_HOST'] = config.HOST
mysql.init_app(app)

conn = mysql.connect()

import mind.routes.clinic
import mind.routes.user
import mind.routes.event
