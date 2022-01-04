import requests
from APITestingWithRequests.utilities import payloads
from APITestingWithRequests.utilities.config import get_config

add_url = get_config()['API']['BaseURL'] + get_config()['API']['AddResource']
add_book_response = requests.post(add_url, json=payloads.get_add_json_payload(), )
add_book_response = add_book_response.json()
assert 'successfully added' in add_book_response['Msg']
added_book_ID = add_book_response['ID']

delete_url = get_config()['API']['BaseURL'] + get_config()['API']['DeleteResource']
delete_response = requests.post(delete_url, json={'ID': added_book_ID}, )
delete_response = delete_response.json()
assert 'book is successfully deleted' in delete_response['msg']
