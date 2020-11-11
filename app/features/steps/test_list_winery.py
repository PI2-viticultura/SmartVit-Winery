from behave import given, when, then
import requests

api_url=None

@given('a pagina de gerenciar vinicolas')
def step_impl_given(context):
    global api_url
    api_url = 'https://smartvit-winery-dev.herokuapp.com/winery'
    print('url :'+api_url)

@when('ele visualizar as vinicolas desejadas')
def step_impl_when(context):
    response = requests.get('https://smartvit-winery-dev.herokuapp.com/winery')
    assert response.status_code == 200


@then('o bff requisita o microsservico desejado')
def step_impl_then(context):
    response = requests.get('https://smartvit-admin-bff-dev.herokuapp.com/winery/')
    assert response.status_code == 200
