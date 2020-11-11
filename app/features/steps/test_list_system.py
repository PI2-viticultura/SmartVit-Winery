from behave import given, when, then
import requests

api_url=None

@given('a pagina de gerenciar sistemas')
def step_impl_given(context):
    global api_url
    api_url = 'https://smartvit-winery-dev.herokuapp.com/system'
    print('url :'+api_url)

@when('ele visualizar os sistemas desejados')
def step_impl_when(context):
    response = requests.get('https://smartvit-winery-dev.herokuapp.com/system')
    assert response.status_code == 200


@then('o bff requisita o microsservico do sistema')
def step_impl_then(context):
    response = requests.get('https://smartvit-admin-bff-dev.herokuapp.com/bff')
    assert response.status_code == 200
