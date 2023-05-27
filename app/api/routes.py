from . import billing_api_blueprint
from .. import db
from ..models import Bill
from flask import request, jsonify


@billing_api_blueprint.route("/api/bills", methods=["GET"])
def get_bills():
    bills = Bill.query.all()
    return jsonify([bill.to_json() for bill in bills])


@billing_api_blueprint.route("/api/bills/add", methods=["POST"])
def add_bill():
    user_name = request.form["user_name"]
    concept = request.form["concept"]
    ammount = request.form["ammount"]
    date = request.form["date"]
    bill = Bill()
    bill.user_name = user_name
    bill.concept = concept
    bill.ammount = ammount
    bill.date = date

    db.session.add(bill)
    db.session.commit()
    return jsonify({"status": "success", "bill": bill.to_json()})
