from application.controllers import BusinessController
from application.models import Business
from flask import Blueprint, request, jsonify, session
from application import bcrypt


business = Blueprint("business", __name__)


@business.route("/")
def get_businesses():
    businesses = BusinessController.get_all_businesses()
    business_list = []
    for business in businesses:
        business_list.append(format_business(business))
    return jsonify(business_list), 200


def format_business(business):
    return {
        "id": business.business_id,
        "business_name": business.business_name,
        "password": business.business_password,
    }


@business.route("/<business_id>", methods=["GET"])
def get_business_by_id(business_id):
    business = BusinessController.get_one_by_business_id(business_id)
    if business:
        return jsonify(format_business(business))
    else:
        return jsonify({"message": "Business not found"})


@business.route("/update/<int:business_id>", methods=["PUT"])
def update_business(business_id):
    data = request.json
    business_name = data.get("business_name")
    password = data.get("password")
    BusinessController.update_user(business_id, business_name, password)
    return jsonify({"message": "Business updated successfully"})


@business.route("/delete/<int:business_id>", methods=["DELETE"])
def delete_business(business_id):
    BusinessController.delete_user(business_id)
    return jsonify({"message": "Business deleted successfully"})


@business.route("/register", methods=["POST"])
def register_business():
    data = request.json
    # print(data)
    business_name = data.get("business_name")
    email = data.get("business_email")
    number = data.get("business_number")
    password = data.get("business_password")

    business_exist = (
        Business.query.filter_by(business_name=business_name).first() is not None
    )

    if business_exist:
        return jsonify({"error": "Business already exist"})

    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
    new_business = Business(
        business_name=business_name,
        business_password=hashed_password,
        business_email=email,
        business_number=number,
    )

    session["user_id"] = new_business.business_id

    BusinessController.register_business(business_name, hashed_password, email, number)
    return jsonify(
        {
            "business_name": business_name,
            "password": hashed_password,
            "number": number,
            "email": email,
        }
    )


@business.route("/login", methods=["POST"])
def login_business():
    data = request.json
    business_name = data.get("business_name")
    password = data.get("business_password")

    business = Business.query.filter_by(business_name=business_name).first()

    if business is None:
        return jsonify({"error": "Unauthorized access"}), 401

    if not bcrypt.check_password_hash(business.business_password, password):
        return jsonify({"error": "Unauthorized"}), 401

    session["business_id"] = business.business_id

    return jsonify({"business_name": business_name})
