def validate_fields(request):
    fields = ['name', 'address', 'contract_id']
    return all(field in request.keys() for field in fields)


def validate_name(request):
    return request["name"]


def validate_address(request):
    return request["address"]


def validate_contract(request):
    return request["contract_id"]
