from behave import given, when, then
import requests

api_url=None

@given('a pagina de gerenciar sensores')
def step_impl_given(context):
    global api_url
    api_url = 'https://smartvit-winery-dev.herokuapp.com/sensor'
    print('url :'+api_url)

@when('ele visualizar os sensores desejados')
def step_impl_when(context):
    response = requests.get('https://smartvit-winery-dev.herokuapp.com/sensor')
    assert response.status_code == 200


@then('o bff requisita o microsservico do sensor')
def step_impl_then(context):
    response = requests.get('https://smartvit-admin-bff-dev.herokuapp.com/sensor')
    assert response.status_code == 200
