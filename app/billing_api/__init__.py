from flask import Flask
from flask import Blueprint

billing_api_blueprint = Blueprint("billing_api", __name__)

from . import routes
