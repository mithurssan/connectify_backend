from application.controllers import RotaController
from flask import Blueprint, abort, request
from flask import jsonify

rota = Blueprint("rota", __name__)


@rota.route("/", methods=["GET"])
def get_users():
    rotas = RotaController.get_all_rotas()
    rota_list = []
    for rota in rotas:
        rota_list.append(format_rotas(rota))
    return jsonify(rota_list)


def format_rotas(rota):
    return {
        "rota_id": rota.rota_id,
        "business_id": rota.business_id,
        "rota_start_date": rota.rota_start_date,
        "rota_end_date": rota.rota_end_date,
        "rota_content": rota.rota_content,
    }


@rota.route("/get/<string:business_id>", methods=["GET"])
def get_rotas_by_business_id(business_id):
    rotas = RotaController.get_rotas_by_business_id(business_id)
    rota_list = []
    if rotas:
        for rota in rotas:
            rota_list.append(format_rotas(rota))
        return jsonify(rota_list)
    else:
        abort(404, "No Rotas found for this business")


@rota.route("/add", methods=["POST"])
def create_rota():
    data = request.get_json()
    business_id = data["business_id"]
    rota_start_date = data["rota_start_date"]
    rota_end_date = data["rota_end_date"]
    rota_content = data["rota_content"]

    RotaController.post_rota(business_id, rota_start_date, rota_end_date, rota_content)
    return jsonify({"message": "Rota added."})


@rota.route("/<rota_id>", methods=["GET"])
def get_user_by_id(rota_id):
    rota = RotaController.get_one_by_rota_id(rota_id)
    if rota:
        return jsonify(format_rotas(rota))
    else:
        abort(404, "Rota not found")


@rota.route("/update/<int:rota_id>", methods=["PUT"])
def update_rota(rota_id):
    data = request.json
    business_id = data["business_id"]
    rota_start_date = data["rota_start_date"]
    rota_end_date = data["rota_end_date"]
    rota_content = data["rota_content"]
    RotaController.update_rota(
        rota_id, business_id, rota_start_date, rota_end_date, rota_content
    )
    return jsonify({"message": "Rota updated successfully"})


@rota.route("/delete/<int:rota_id>", methods=["DELETE"])
def delete_rota(rota_id):
    RotaController.delete_rota(rota_id)
    return jsonify({"message": "Rota deleted successfully"})
