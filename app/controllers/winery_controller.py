from models.winery import MongoDB
from utils.validators import (
    validate_fields, validate_name, validate_address, validate_contract
)
from bson import ObjectId


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
        del request['contract_id']
        contract = db.get_one(contract_id, 'contracts')

        if not contract:
            return {"erro": "Insira um contrato válido"}, 400

        if not contract['winery']:
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


def update_winery_request(id, request):
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

    id = ObjectId(id)
    contract_id = ObjectId(request['contract_id'])
    del request['contract_id']

    db = MongoDB()
    connection_is_alive = db.test_connection()

    contract = db.get_one(contract_id, 'contracts')
    if not contract:
        return {"erro": "Insira um contrato válido"}, 400

    if connection_is_alive:
        if(db.update_one(id, request)):
            winery = db.get_one(id, 'winery')
            contract['winery'] = winery
            if(db.update_one(contract_id, contract, 'contracts')):
                return {"message": "success"}, 200

    db.close_connection()

    return {'error': 'Something gone wrong'}, 500
