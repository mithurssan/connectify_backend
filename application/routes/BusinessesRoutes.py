from application.controllers import BusinessController
from application.models import Business
from flask import Blueprint, request, jsonify, session
from application import bcrypt
from flask_jwt_extended import jwt_required, create_access_token

business = Blueprint("business", __name__)


@business.route("/")
@jwt_required()
def get_businesses():
    businesses = BusinessController.get_all_businesses()
    business_list = []
    for business in businesses:
        business_list.append(format_business(business))
    return jsonify(business_list), 200


def format_business(business):
    return {
        "business_id": business.business_id,
        "business_email": business.business_email,
        "business_name": business.business_name,
        "business_password": business.business_password,
    }


@business.route("/<string:business_id>", methods=["GET"])
def get_business_by_id(business_id):
    business = BusinessController.get_one_by_business_id(business_id)
    if business:
        return jsonify(format_business(business))
    else:
        return jsonify({"message": "Business not found"}), 404


@business.route("/update/<string:business_id>", methods=["PUT"])
def update_business(business_id):
    data = request.json
    business_email = data['business_email']
    business_name = data['business_name']
    business_password = data['business_password']
    BusinessController.update_business(business_id, business_email, business_name, business_password)
    return jsonify({"message": "Business updated successfully"})


@business.route("/delete/<string:business_id>", methods=["DELETE"])
def delete_business(business_id):
    BusinessController.delete_business(business_id)
    return jsonify({"message": "Business deleted successfully"})


@business.route("/register", methods=["POST"])
def register_business():
    data = request.json
    # print(data)
    business_email = data.get("business_email")
    business_name = data.get("business_name")
    business_number = data.get("business_number")
    business_password = data.get("business_password")

    business_exist = (
        Business.query.filter_by(business_name=business_name).first() is not None
    )

    if business_exist:
        return jsonify({"error": "Business already exists"})

    hashed_password = bcrypt.generate_password_hash(business_password).decode("utf-8")
    new_business = Business(
        business_name=business_name,
        business_password=hashed_password,
        business_email=business_email,
        business_number=business_number,
    )

    session["user_id"] = new_business.business_id

    BusinessController.register_business(business_name, hashed_password, business_email, business_number)
    return jsonify(
        {
            "business_name": business_name,
            "business_password": business_password,
            "business_number": business_number,
            "business_email": business_email,
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
    access_token = create_access_token(identity=business_name)
    session["business_id"] = business.business_id

    return jsonify({"business_id": business.business_id, "business_name": business_name, "token": access_token})
