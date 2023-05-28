# app/routes.py
from flask import Flask

from adapters.controllers.billController import billBP

app = Flask(__name__)
app.register_blueprint(billBP)

app.run()
