from behave import given, when, then
import requests

request_headers = {}
request_bodies = {}
api_url = None
bff_url = None


@given('a pagina de criar novo sensor')
def step_impl_given(context):
    global api_url
    api_url = 'https://smartvit-winery-stg.herokuapp.com/sensor'
    print('url :'+api_url)


@when('ele regista novo conteudo do sensor da solicitacao')
def step_impl_when(context):
    request_bodies['POST'] = {"location": "Norte",
                              "identifier": "KXY",
                              "type": "Series X",
                              "situation": "Ativo",
                              "system_id": "5fadfec0b2126679ab246983"}
    response = requests.post(
                            'https://smartvit-winery-stg.herokuapp.com/sensor',
                            json=request_bodies['POST']
                            )
    assert response.status_code == 200


@then('o bff requisita o microsservico para criar informacao do sensor')
def step_impl_then(context):
    global bff_url
    bff_url = 'https://smartvit-admin-bff-stg.herokuapp.com/sensor'
    response = requests.post(
                            bff_url,
                            json=request_bodies['POST']
                            )
    assert response.status_code == 200
