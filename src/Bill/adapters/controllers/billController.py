# app/controllers/user_controller.py
from flask import Blueprint, request, jsonify
from application.Services.billService import BillService
from adapters.DTO.billDTO import BillDTO

billBP = Blueprint("bills", __name__)


@billBP.route("/bills", methods=["POST"])
def create_bill():
    data = request.get_json()
    billDto = BillDTO(data["user_name"], data["concept"], data["ammount"], data["date"])
    bill_service = BillService()
    bill = bill_service.createBill(billDto)
    if bill:
        response = {
            "message": "Bill created successfully",
            "billID": bill.billID,
            "user_name": bill.user_name,
            "concept": bill.concept,
            "ammount": bill.ammount,
            "date": bill.date,
        }
        return jsonify(response), 201
    else:
        return jsonify({"message": "Failed to create bill"}), 500


@billBP.route("/bills/<int:billID>", methods=["GET"])
def get_bill(billID):
    bill_service = BillService()
    billDto = BillDTO(billID)
    bill = bill_service.getBill(billDto)
    if bill:
        response = {
            "billID": bill.billID,
            "user_name": bill.user_name,
            "concept": bill.concept,
            "ammount": bill.ammount,
            "date": bill.date,
        }
        return jsonify(response), 200
    else:
        return jsonify({"message": "Bill not found"}), 404


@billBP.route("/bills/<int:billID>", methods=["PUT"])
def update_bill(userID):
    data = request.get_json()
    billDto = BillDTO(
        userID, data["user_name"], data["concept"], data["ammount"], data["date"]
    )

    bill_service = BillService()  # Instancia del servicio de usuario
    bill = bill_service.updateBill(billDto)

    if bill:
        response = {
            "message": "Bill updated successfully",
            "billID": bill.billID,
            "user_name": bill.user_name,
            "concept": bill.concept,
            "ammount": bill.ammount,
            "date": bill.date,
        }
        return jsonify(response), 200
    else:
        return jsonify({"message": "Bill not found"}), 404


@billBP.route("/bills/<int:billID>", methods=["DELETE"])
def delete_bill(billID):
    bill_service = BillService()
    billDto = BillDTO(billID)
    bill_service.deleteBill(billDto)
    return jsonify({"message": "Bill deleted successfully"}), 200


@billBP.route("/bills/usernamechange", methods=["PUT"])
def change_username():
    data = request.get_json()
    billDto = BillDTO(data["billID"], data["user_name"])
    userDTO = BillDTO(data["userID"], data["new_user_name"])

    bill_service = BillService()
    bill = bill_service.changeUsername(billDto)
    if bill:
        response = {
            "message": "Username changed successfully",
            "billID": bill.billID,
            "user_name": bill.user_name,
            "concept": bill.concept,
            "ammount": bill.ammount,
            "date": bill.date,
        }
        return jsonify(response), 200
    else:
        return jsonify({"message": "Bill not found"}), 404
