from models.winery import MongoDB
from utils.validators import (
    validate_fields, validate_name, validate_address, validate_contract
)
from bson.json_util import dumps
from bson import ObjectId


def get_all_winery():
    db = MongoDB()
    connection_is_alive = db.test_connection()
    if connection_is_alive:
        winery = db.get_all('winery')
        if winery:
            return dumps(winery), 200

        return {'error': 'Winery not found'}, 404

    return {'error': 'Something gone wrong'}, 500


def save_winery_request(request):
    if not validate_fields(request):
        return {
            "erro": "Sua requisição não informou todos os campos necessários"
        }, 400

    if not validate_name(request):
        return {"erro": "Não é possível enviar nome vazio"}, 400

    if not validate_address(request):
        return {"erro": "Não é possível enviar endereço vazio"}, 400

    if not validate_contract(request):
        return {"erro": "Não é possível enviar contrato vazio"}, 400

    db = MongoDB()
    connection_is_alive = db.test_connection()
    if connection_is_alive:
        contract_id = ObjectId(request['contract_id'])
        request.pop('contract_id', None)
        contract = db.get_one(contract_id, 'contracts')


        if not contract:
            return {"erro": "Insira um contrato válido"}, 400

        if 'winery' not in contract.keys():
            winery = db.insert_one(request)
            if(winery):
                winery = db.get_one(winery.inserted_id, 'winery')
        
        elif not contract['winery']:
            winery = db.insert_one(request)
            if(winery):
                winery = db.get_one(winery.inserted_id, 'winery')

        else:
            if(db.update_one(contract['winery']['_id'], request)):
                winery = db.get_one(contract['winery']['_id'], 'winery')
                contract['winery'] = winery

        if winery:
            contract['winery'] = winery
            if(db.update_one(contract_id, contract, 'contracts')):
                return {"message": "success"}, 200

    db.close_connection()

    return {'error': 'Something gone wrong'}, 500


def update_winery_request(winery_id, request):
    if not validate_fields(request):
        return {
            "erro": "Sua requisição não informou todos os campos necessários"
        }, 400

    if not validate_name(request):
        return {"erro": "Não é possível enviar nome vazio"}, 400

    if not validate_address(request):
        return {"erro": "Não é possível enviar endereço vazio"}, 400

    if not validate_contract(request):
        return {"erro": "Não é possível enviar contrato vazio"}, 400

    winery_id = ObjectId(winery_id)
    contract_id = ObjectId(request['contract_id'])
    request.pop('contract_id', None)

    db = MongoDB()
    connection_is_alive = db.test_connection()

    if connection_is_alive:
        contract = db.get_one(contract_id, 'contracts')
        if not contract:
            return {"erro": "Insira um contrato válido"}, 400

        if(db.update_one(winery_id, request)):
            winery = db.get_one(winery_id, 'winery')
            contract['winery'] = winery
            if(db.update_one(contract_id, contract, 'contracts')):
                return {"message": "success"}, 200

    db.close_connection()

    return {'error': 'Something gone wrong'}, 500


def toggle_winery_request(winery_id):
    winery_id = ObjectId(winery_id)

    db = MongoDB()
    connection_is_alive = db.test_connection()

    if connection_is_alive:
        winery = db.get_one(winery_id, 'winery')
        if not winery:
            return {'error': 'Winery not found'}, 204

        if 'active' not in winery.keys():
            winery['active'] = False
        else:
            winery['active'] = not winery['active']

        if(db.update_one(winery_id, winery)):
            contract = db.get_contract_by_winery_id(winery_id)
            if contract:
                contract['winery'] = winery
                if(db.update_one(contract['_id'], contract, 'contracts')):
                    return {"message": "success"}, 200

    db.close_connection()

    return {'error': 'Something gone wrong'}, 500
