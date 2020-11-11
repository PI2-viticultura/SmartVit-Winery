from behave import given, when, then
import requests

request_headers = {}
request_bodies = {}
api_url = None


@given('a pagina de criar novo sensor')
def step_impl_given(context):
    global api_url
    api_url = 'https://smartvit-winery-dev.herokuapp.com/sensor'
    print('url :'+api_url)


@when('ele regista novo conteudo do sensor da solicitacao')
def step_impl_when(context):
    request_bodies['POST'] = {"location": "Norte",
                              "identifier": "KXY",
                              "type": "Series X",
                              "situation": "Ativo",
                              "system_id": "5f9ee3c0b62731672936ca28"
                             }
    response = requests.post(
                            'https://smartvit-winery-dev.herokuapp.com/sensor',
                             json=request_bodies['POST']
                            )
    assert response.status_code == 200


@then('o bff requisita o microsservico para criar informacao do sensor')
def step_impl_then(context):
    response = requests.post(
                            'https://smartvit-admin-bff-dev.herokuapp.com/sensor',
                             json=request_bodies['POST']
                            )
    assert response.status_code == 200
