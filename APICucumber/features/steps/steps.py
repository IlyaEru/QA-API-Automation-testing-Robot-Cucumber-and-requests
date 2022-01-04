import requests
from behave import *
from APICucumber.utilities.payloads import *
from APICucumber.utilities.getConfig import get_config


@given('the place details which needs to be added to the server')
def step_impl(context):
    context.add_url = get_config()['API']['BaseURL'] + get_config()['API']['AddResource']
    context.add_payload = get_add_json_payload()
    context.add_param = {"key": "qaclick123"}


@when("we execute the Google Maps PostAPI method")
def step_impl(context):
    context.add_response = requests.post(context.add_url, context.add_payload,)


@then("place is successfully added")
def step_impl(context):
    context.add_response = context.add_response.json()
    assert context.add_response['status'] == 'OK'
    context.place_id = context.add_response['place_id']

