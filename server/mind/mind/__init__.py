from flask import Flask
app = Flask(__name__)

app.debug = True
import mind.routes.clinic
import mind.routes.user
import mind.routes.event
