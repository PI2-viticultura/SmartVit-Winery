from flask import Blueprint, request
from flask_cors import CORS
import controllers.winery_controller as controller

app = Blueprint('winery', __name__)
CORS(app)


@app.route("/winery", methods=["POST", "GET"])
def winery():
    if request.method == "POST":
        return controller.save_winery_request(request.json)
    elif request.method == "GET":
        return controller.get_all_winery()


@app.route("/winery/<string:id>", methods=["PUT", "PATCH"])
def winery_put(id):
    if request.method == "PUT":
        return controller.update_winery_request(id, request.json)
    elif request.method == "PATCH":
        return controller.toggle_winery_request(id)
