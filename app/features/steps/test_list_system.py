from behave import given, when, then
import requests

api_url = None
response_codes = {}


@given('a pagina de gerenciar sistemas')
def step_impl_given(context):
    global api_url
    api_url = 'https://smartvit-winery-dev.herokuapp.com/system'
    print('url :'+api_url)


@when('ele visualizar os sistemas desejados')
def step_impl_when(context):
    response = requests.get('https://smartvit-winery-dev.herokuapp.com/system')
    statuscode = response.status_code
    response_codes['GET'] = statuscode


@then('confirma se a listagem do sistema foi pega')
def step_impl_then(context):
    print('GET rep code ;'+str(response_codes['GET']))
    assert response_codes['GET'] is 200
