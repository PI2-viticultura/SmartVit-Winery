def validate_fields(request):
    fields = ['name', 'address', 'contract_id']
    return all(field in request.keys() for field in fields)


def validate_name(request):
    return request["name"]


def validate_address(request):
    return request["address"]


def validate_contract(request):
    return request["contract_id"]


def validate_fields_system(request):
    fields = ['latitude', 'longitude', 'status', 'winery_id']
    return all(field in request.keys() for field in fields)


def validate_latitude(request):
    return request["latitude"]


def validate_longitude(request):
    return request["longitude"]


def validate_status(request):
    return request["status"]


def validate_winery(request):
    return request["winery_id"]


def validate_fields_sensor(request):
    fields = ['identifier', 'type', 'system_id']
    return all(field in request.keys() for field in fields)


def validate_identifier(request):
    return request["identifier"]


def validate_type(request):
    return request["type"]


def validate_system_id(request):
    return request["system_id"]
