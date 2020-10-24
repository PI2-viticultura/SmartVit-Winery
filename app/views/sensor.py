from flask import Blueprint, request
from flask_cors import CORS
import controllers.sensor_controller as controller

app = Blueprint('sensor', __name__)
CORS(app)


@app.route("/sensor", methods=["POST", "GET"])
def sensor():
    if request.method == "POST":
        return controller.save_sensor_request(request.json)
    elif request.method == "GET":
        return controller.get_all_sensor()


@app.route("/sensor/<string:identity>", methods=["PUT", "PATCH"])
def sensor_put(identity):
    if request.method == "PUT":
        return controller.update_sensor_request(identity, request.json)
    elif request.method == "PATCH":
        return controller.toggle_sensor_request(identity)
