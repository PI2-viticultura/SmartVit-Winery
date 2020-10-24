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
        system_id = ObjectId(request['system_id'])
        request.pop('system_id', None)
        system = db.get_one(system_id, 'winery')

        if not system:
            return {"erro": "Insira um sistema válido"}, 400

        if not system['sensor']:
            sensor = db.insert_one(request)
            if(sensor):
                sensor = db.get_one(sensor.inserted_id, 'sensor')

        else:
            if(db.update_one(system['sensor']['_id'], request)):
                sensor = db.get_one(system['sensor']['_id'], 'sensor')
                system['sensor'] = sensor

        if sensor:
            system['sensor'] = sensor
            if(db.update_one(system_id, system, 'winery')):
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
    system_id = ObjectId(request['system_id'])
    request.pop('system_id', None)

    db = MongoDB()
    connection_is_alive = db.test_connection()

    if connection_is_alive:
        system = db.get_one(system_id, 'winery')
        if not system:
            return {"erro": "Insira um Sistema válido"}, 400

        if(db.update_one(sensor_id, request)):
            sensor = db.get_one(sensor_id, 'sensor')
            system['sensor'] = sensor
            if(db.update_one(system_id, system, 'winery')):
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
            system = db.get_system_by_sensor_id(sensor_id)
            if system:
                system['sensor'] = sensor
                if(db.update_one(system['_id'], system, 'winery')):
                    return {"message": "success"}, 200

    db.close_connection()

    return {'error': 'Something gone wrong'}, 500
