from models.sensor import MongoDB
from utils.validators import (
    validate_fields_sensor, validate_identifier,
    validate_type, validate_system_id
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

    if not validate_identifier(request):
        return {"erro": "Não é possível enviar identificador vazio"}, 400

    if not validate_type(request):
        return {"erro": "Não é possível enviar tipo do sensor vazio"}, 400

    if not validate_system_id(request):
        return {"erro": "Não é possível enviar id de sistema vazio"}, 400

    db = MongoDB()
    connection_is_alive = db.test_connection()
    if connection_is_alive:
        system_id = ObjectId(request['system_id'])
        request.pop('system_id', None)
        system = db.get_one(system_id, 'system')

        if not system:
            return {"erro": "Insira um sistema válido"}, 400

        if 'sensors' not in system.keys():
            system['sensors'] = []

        sensor = db.insert_one(request)
        if(sensor):
            sensor = db.get_one(sensor.inserted_id, 'sensor')

        if sensor:
            system['sensors'].append(sensor)
            if(db.update_one(system_id, system, 'system')):
                winery = db.get_winery_by_system_id(system_id)
                if winery:
                    if 'systems' not in winery.keys():
                        winery['systems'] = []

                    system_index = -1
                    count = -1
                    for system_item in winery['systems']:
                        count += 1
                        if system_item['_id'] == system_id:
                            system_index = count

                    if system_index != -1:
                        winery['systems'][system_index] = system
                    else:
                        winery['systems'].append(system)

                    if(db.update_one(winery['_id'], winery, 'winery')):
                        return {"message": "success"}, 200

    db.close_connection()

    return {'error': 'Something gone wrong'}, 500


def update_sensor_request(sensor_id, request):
    if not validate_fields_sensor(request):
        return {
            "erro": "Sua requisição não informou todos os campos necessários"
        }, 400

    if not validate_identifier(request):
        return {"erro": "Não é possível enviar identificador vazio"}, 400

    if not validate_type(request):
        return {"erro": "Não é possível enviar tipo do sensor vazio"}, 400

    if not validate_system_id(request):
        return {"erro": "Não é possível enviar id de sistema vazio"}, 400

    sensor_id = ObjectId(sensor_id)
    system_id = ObjectId(request['system_id'])
    request.pop('system_id', None)

    db = MongoDB()
    connection_is_alive = db.test_connection()

    if connection_is_alive:
        system = db.get_one(system_id, 'system')
        if not system:
            return {"erro": "Insira um Sistema válido"}, 400

        if(db.update_one(sensor_id, request)):
            sensor_index = -1
            count = -1
            for sensor_item in system['sensors']:
                count += 1
                if sensor_item['_id']['$oid'] == sensor_id:
                    sensor_index = count

            sensor = db.get_one(sensor_id, 'sensor')
            if sensor_index != -1:
                system['sensors'][sensor_index] = sensor
            else:
                system['sensors'].append(sensor)

            if(db.update_one(system_id, system, 'system')):
                winery = db.get_winery_by_system_id(system_id)
                if winery:
                    if 'systems' not in winery.keys():
                        winery['systems'] = []

                    system_index = -1
                    count = -1
                    for system_item in winery['systems']:
                        count += 1
                        if system_item['_id'] == system_id:
                            system_index = count

                    if system_index != -1:
                        winery['systems'][system_index] = system
                    else:
                        winery['systems'].append(system)

                    if(db.update_one(winery['_id'], winery, 'winery')):
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
                sensor_index = -1
                count = -1
                for sensor_item in system['sensors']:
                    count += 1
                    if sensor_item['_id'] == sensor_id:
                        sensor_index = count

                if sensor_index != -1:
                    system['sensors'][sensor_index] = sensor
                else:
                    system['sensors'].append(sensor)

                if(db.update_one(system['_id'], system, 'system')):
                    return {"message": "success"}, 200

    db.close_connection()

    return {'error': 'Something gone wrong'}, 500
