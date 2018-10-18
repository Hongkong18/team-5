from flask import Flask
from flaskext.mysql import MySQL
import config

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = config.USER
app.config['MYSQL_DATABASE_PASSWORD'] = config.PASSWORD
app.config['MYSQL_DATABASE_DB'] = config.DB
app.config['MYSQL_DATABASE_HOST'] = config.HOST
mysql.init_app(app)

conn = mysql.connect()


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
