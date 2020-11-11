from behave import given, when, then
import requests

request_headers = {}
request_bodies = {}
api_url = None


@given('a pagina de criar novo sistema')
def step_impl_given(context):
    global api_url
    api_url = 'https://smartvit-winery-dev.herokuapp.com/system'
    print('url :'+api_url)


@when('ele regista novo conteudo do sistema da solicitacao')
def step_impl_when(context):
    request_bodies['POST'] = {"latitude": 1454.55,
                              "longitude": 154895.12,
                              "status": "Desativado",
                              "winery_id": "5fa0c880d578d4bc349dc376"
                             }
    response = requests.post(
                            'https://smartvit-winery-dev.herokuapp.com/system',
                             json=request_bodies['POST']
                            )
    assert response.status_code == 200


@then('o bff requisita o microsservico para criar informacao do sistema')
def step_impl_then(context):
    response = requests.post(
                            'https://smartvit-admin-bff-dev.herokuapp.com/bff',
                             json=request_bodies['POST']
                            )
    assert response.status_code == 200
