from models.winery import MongoDB
from utils.validators import validate_fields, validate_name, validate_address
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

    db = MongoDB()
    connection_is_alive = db.test_connection()
    if connection_is_alive:
        if(db.insert_one(request)):
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
    
    id = ObjectId(id)
    db = MongoDB()
    connection_is_alive = db.test_connection()
    if connection_is_alive:
        if(db.update_one(id, request)):
            return {"message": "success"}, 200
    db.close_connection()

    return {'error': 'Something gone wrong'}, 500