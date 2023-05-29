# app/controllers/user_controller.py
from flask import Blueprint, request, jsonify
from application.Services.billService import BillService
from adapters.DTO.billDTO import BillDTO
from adapters.DTO.userDTO import UserDTO


billBP = Blueprint("bills", __name__)


@billBP.route("/bills", methods=["POST"])
def create_bill():
    data = request.get_json()
    billDto = BillDTO(
        billUserID=data["userID"],
        billConcept=data["concept"],
        billAmount=data["amount"],
        billDate=data["date"],
    )
    bill_service = BillService()
    bill = bill_service.createBill(billDto)
    if bill != 404 and bill:
        response = {
            "message": "Bill created successfully",
            "billID": bill.billID,
            "userID": bill.userID,
            "concept": bill.concept,
            "amount": bill.amount,
            "date": bill.date,
        }
        return jsonify(response), 201
    elif bill == 404:
        return jsonify({"message": "User not found"}), 404
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
            "userID": bill.userID,
            "concept": bill.concept,
            "amount": bill.amount,
            "date": bill.date,
        }
        return jsonify(response), 200
    else:
        return jsonify({"message": "Bill not found"}), 404


@billBP.route("/bills/<int:billID>", methods=["PUT"])
def update_bill(billID):
    data = request.get_json()
    billDto = BillDTO(
        billID, data["userID"], data["concept"], data["amount"], data["date"]
    )

    bill_service = BillService()  # Instancia del servicio de usuario
    bill = bill_service.updateBill(billDto)

    if bill != 404 and bill:
        response = {
            "message": "Bill updated successfully",
            "billID": bill.billID,
            "userID": bill.userID,
            "concept": bill.concept,
            "amount": bill.amount,
            "date": bill.date,
        }
        return jsonify(response), 200
    elif bill == 404:
        return jsonify({"message": "User not found"}), 404
    else:
        return jsonify({"message": "Bill not found"}), 404


@billBP.route("/bills/<int:billID>", methods=["DELETE"])
def delete_bill(billID):
    bill_service = BillService()
    billDto = BillDTO(billID)
    bill_service.deleteBill(billDto)
    return jsonify({"message": "Bill deleted successfully"}), 200


@billBP.route("/bills/deletefromuser/<int:userID>", methods=["DELETE"])
def delete_bill_from_user(userID):
    bill_service = BillService()
    billDto = BillDTO(billUserID=userID)
    bill_service.deleteBillFromUser(billDto)
    print("TRYING TO DELETE !!!!!!!!!!")
    return jsonify({"message": "Bill deleted successfully"}), 200
