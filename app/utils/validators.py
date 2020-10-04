def validate_fields(request):
    fields = ['name', 'address']
    return all(field in request.keys() for field in fields)


def validate_name(request):
    return request["name"]


def validate_address(request):
    return request["address"]
