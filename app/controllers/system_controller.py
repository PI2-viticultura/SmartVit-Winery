from models.system import MongoDB
from utils.validators import (
    validate_fields_system, validate_latitude, validate_longitude,
    validate_status, validate_winery
)
from bson.json_util import dumps
from bson import ObjectId


def get_all_system():
    db = MongoDB()
    connection_is_alive = db.test_connection()
    if connection_is_alive:
        system = db.get_all('system')
        if system:
            return dumps(system), 200

        return {'error': 'System not found'}, 404

    return {'error': 'Something gone wrong'}, 500


def save_system_request(request):
    if not validate_fields_system(request):
        return {
            "erro": "Sua requisição não informou todos os campos necessários"
        }, 400

    if not validate_latitude(request):
        return {"erro": "Não é possível enviar latitude vazia"}, 400

    if not validate_longitude(request):
        return {"erro": "Não é possível enviar longitude vazia"}, 400

    if not validate_status(request):
        return {"erro": "Não é possível enviar status vazio"}, 400

    if not validate_winery(request):
        return {"erro": "Não é possível enviar vinícola vazia"}, 400

    db = MongoDB()
    connection_is_alive = db.test_connection()
    if connection_is_alive:
        winery_id = ObjectId(request['winery_id'])
        request.pop('winery_id', None)
        winery = db.get_one(winery_id, 'winery')

        if not winery:
            return {"erro": "Insira uma vinícola válida"}, 400

        if 'systems' not in winery.keys():
            winery['systems'] = []

        system = db.insert_one(request)
        if(system):
            system = db.get_one(system.inserted_id, 'system')

        if system:
            winery['systems'].append(system)
            if(db.update_one(winery_id, winery, 'winery')):
                return {"message": "success"}, 200

    db.close_connection()

    return {'error': 'Something gone wrong'}, 500


def update_system_request(system_id, request):
    if not validate_fields_system(request):
        return {
            "erro": "Sua requisição não informou todos os campos necessários"
        }, 400

    if not validate_latitude(request):
        return {"erro": "Não é possível enviar latitude vazia"}, 400

    if not validate_longitude(request):
        return {"erro": "Não é possível enviar longitude vazia"}, 400

    if not validate_status(request):
        return {"erro": "Não é possível enviar status vazio"}, 400

    if not validate_winery(request):
        return {"erro": "Não é possível enviar vinícola vazia"}, 400

    system_id = ObjectId(system_id)
    winery_id = ObjectId(request['winery_id'])
    request.pop('winery_id', None)

    db = MongoDB()
    connection_is_alive = db.test_connection()

    if connection_is_alive:
        winery = db.get_one(winery_id, 'winery')
        if not winery:
            return {"erro": "Insira uma vinícola válida"}, 400
        
        if 'systems' not in winery.keys():
            winery['systems'] = []

        if(db.update_one(system_id, request)):
            system_index = -1
            count = -1
            for system in winery['systems']:
                count += 1
                if system['_id'] == system_id:
                    system_index = count

            system = db.get_one(system_id, 'system')
            if system_index != -1:
                winery['systems'][system_index] = system
            else:
                winery['systems'].append(system)

            if(db.update_one(winery_id, winery, 'winery')):
                return {"message": "success"}, 200
            

    db.close_connection()

    return {'error': 'Something gone wrong'}, 500


def toggle_system_request(system_id):
    system_id = ObjectId(system_id)

    db = MongoDB()
    connection_is_alive = db.test_connection()

    if connection_is_alive:
        system = db.get_one(system_id, 'system')
        if not system:
            return {'error': 'system not found'}, 204

        if 'active' not in system.keys():
            system['active'] = False
        else:
            system['active'] = not system['active']


        if(db.update_one(system_id, system)):
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
