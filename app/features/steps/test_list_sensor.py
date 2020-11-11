from behave import given, when, then
import requests

api_url = None
response_codes = {}


@given('a pagina de gerenciar sensores')
def step_impl_given(context):
    global api_url
    api_url = 'https://smartvit-winery-dev.herokuapp.com/sensor'
    print('url :'+api_url)


@when('ele visualizar os sensores desejados')
def step_impl_when(context):
    response = requests.get('https://smartvit-winery-dev.herokuapp.com/sensor')
    statuscode = response.status_code
    response_codes['GET'] = statuscode


@then('confirma se a listagem foi pega')
def step_impl_then(context):
    print('GET rep code ;'+str(response_codes['GET']))
    assert response_codes['GET'] is 200
