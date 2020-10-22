from flask import Blueprint, request
from flask_cors import CORS
import controllers.system_controller as controller

app = Blueprint('system', __name__)
CORS(app)


@app.route("/system", methods=["POST", "GET"])
def system():
    if request.method == "POST":
        return controller.save_system_request(request.json)
    elif request.method == "GET":
        return controller.get_all_system()


@app.route("/system/<string:identity>", methods=["PUT", "PATCH"])
def system_put(identity):
    if request.method == "PUT":
        return controller.update_system_request(identity, request.json)
    elif request.method == "PATCH":
        return controller.toggle_system_request(identity)
