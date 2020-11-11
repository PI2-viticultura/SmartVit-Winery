from behave import given, when, then
import requests

request_headers = {}
request_bodies = {}
api_url = None


@given('a pagina de criar nova vinicola')
def step_impl_given(context):
    global api_url
    api_url = 'https://smartvit-winery-dev.herokuapp.com/winery'
    print('url :'+api_url)


@when('ele regista novo conteudo da solicitacao')
def step_impl_when(context):
    request_bodies['POST'] = {"name": "Vinicola dos Alveres",
                              "address": "Fazendas do Sul - RS",
                              "contract_id": "5f87a04fff9628aaeeea43a9"
                             }
    response = requests.post(
                            'https://smartvit-winery-dev.herokuapp.com/winery',
                             json=request_bodies['POST']
                            )
    assert response.status_code == 200


@then('o bff requisita o microsservico para criar informacao')
def step_impl_then(context):
    response = requests.post(
                            'https://smartvit-admin-bff-dev.herokuapp.com/winery',
                             json=request_bodies['POST']
                            )
    assert response.status_code == 200
