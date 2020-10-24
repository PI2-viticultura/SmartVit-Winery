from models.sensor import MongoDB
from utils.validators import (
    validate_fields_sensor, validate_location, validate_identifier,
    validate_type, validate_situation, validate_system_id
)
from bson.json_util import dumps
from bson import ObjectId


def get_all_sensor():
    db = MongoDB()
    connection_is_alive = db.test_connection()
    if connection_is_alive:
        sensor = db.get_all('sensor')
        if sensor:
            return dumps(sensor), 200

        return {'error': 'sensor not found'}, 404

    return {'error': 'Something gone wrong'}, 500


def save_sensor_request(request):
    if not validate_fields_sensor(request):
        return {
            "erro": "Sua requisição não informou todos os campos necessários"
        }, 400

    if not validate_location(request):
        return {"erro": "Não é possível enviar localização vazia"}, 400

    if not validate_identifier(request):
        return {"erro": "Não é possível enviar identificador vazio"}, 400

    if not validate_type(request):
        return {"erro": "Não é possível enviar tipo de sensor vazio"}, 400

    if not validate_situation(request):
        return {"erro": "Não é possível enviar situação do sensor vazio"}, 400

    if not validate_system_id(request):
        return {"erro": "Não é possível enviar id de sistema vazio"}, 400

    db = MongoDB()
    connection_is_alive = db.test_connection()
    if connection_is_alive:
        winery_id = ObjectId(request['winery_id'])
        request.pop('winery_id', None)
        winery = db.get_one(winery_id, 'winerys')

        if not winery:
            return {"erro": "Insira uma vinícola válida"}, 400

        if not winery['sensor']:
            sensor = db.insert_one(request)
            if(sensor):
                sensor = db.get_one(sensor.inserted_id, 'sensor')

        else:
            if(db.update_one(winery['sensor']['_id'], request)):
                sensor = db.get_one(winery['sensor']['_id'], 'sensor')
                winery['sensor'] = sensor

        if sensor:
            winery['sensor'] = sensor
            if(db.update_one(winery_id, winery, 'winerys')):
                return {"message": "success"}, 200

    db.close_connection()

    return {'error': 'Something gone wrong'}, 500


def update_sensor_request(sensor_id, request):
    if not validate_fields_sensor(request):
        return {
            "erro": "Sua requisição não informou todos os campos necessários"
        }, 400

    if not validate_location(request):
        return {"erro": "Não é possível enviar localização vazia"}, 400

    if not validate_identifier(request):
        return {"erro": "Não é possível enviar identificador vazio"}, 400

    if not validate_type(request):
        return {"erro": "Não é possível enviar tipo de sensor vazio"}, 400

    if not validate_situation(request):
        return {"erro": "Não é possível enviar situação do sensor vazio"}, 400

    if not validate_system_id(request):
        return {"erro": "Não é possível enviar id de sistema vazio"}, 400

    sensor_id = ObjectId(sensor_id)
    winery_id = ObjectId(request['winery_id'])
    request.pop('winery_id', None)

    db = MongoDB()
    connection_is_alive = db.test_connection()

    if connection_is_alive:
        winery = db.get_one(winery_id, 'winerys')
        if not winery:
            return {"erro": "Insira uma vinícola válida"}, 400

        if(db.update_one(sensor_id, request)):
            sensor = db.get_one(sensor_id, 'sensor')
            winery['sensor'] = sensor
            if(db.update_one(winery_id, winery, 'winerys')):
                return {"message": "success"}, 200

    db.close_connection()

    return {'error': 'Something gone wrong'}, 500


def toggle_sensor_request(sensor_id):
    sensor_id = ObjectId(sensor_id)

    db = MongoDB()
    connection_is_alive = db.test_connection()

    if connection_is_alive:
        sensor = db.get_one(sensor_id, 'sensor')
        if not sensor:
            return {'error': 'sensor not found'}, 204

        if 'active' not in sensor.keys():
            sensor['active'] = False
        else:
            sensor['active'] = not sensor['active']

        if(db.update_one(sensor_id, sensor)):
            winery = db.get_winery_by_sensor_id(sensor_id)
            if winery:
                winery['sensor'] = sensor
                if(db.update_one(winery['_id'], winery, 'winerys')):
                    return {"message": "success"}, 200

    db.close_connection()

    return {'error': 'Something gone wrong'}, 500
