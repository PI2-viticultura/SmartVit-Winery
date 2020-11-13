from behave import given, when, then
import requests

request_headers = {}
request_bodies = {}
api_url = None
bff_url = None


@given('a pagina de criar nova vinicola')
def step_impl_given(context):
    global api_url
    api_url = 'https://smartvit-winery-stg.herokuapp.com/winery'
    print('url :'+api_url)


@when('ele regista novo conteudo da solicitacao')
def step_impl_when(context):
    request_bodies['POST'] = {"name": "Vinicola Beta",
                              "address": "Fazendas do Sul - RS",
                              "contract_id": "5fadb2830685d5591099ec2c"}
    response = requests.post(
                            api_url,
                            json=request_bodies['POST']
                            )
    assert response.status_code == 200


@then('o bff requisita o microsservico para criar informacao')
def step_impl_then(context):
    global bff_url
    bff_url = 'https://smartvit-admin-bff-stg.herokuapp.com/winery/'
    response = requests.get(bff_url,
                            json=request_bodies['POST']
                            )
    assert response.status_code == 200
