from . import dog_api_blueprint
from .. import db
from ..models import Bill
from flask import request, jsonify


@dog_api_blueprint.route("/api/bills", methods=["GET"])
def get_bills():
    bills = Bill.query.all()
    return jsonify([bill.to_dict() for bill in bills])
