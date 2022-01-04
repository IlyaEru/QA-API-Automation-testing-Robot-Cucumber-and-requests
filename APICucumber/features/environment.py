import requests
from APICucumber.utilities.getConfig import get_config


def after_scenario(context, scenario):
    if 'googleMaps' in scenario.tags:
        delete_url = get_config()['API']['BaseURL'] + get_config()['API']['DeleteResource']
        delete_response = requests.post(delete_url, json={

            "place_id": context.place_id

        },
                                        )

        assert delete_response.json()['status'] == 'OK'
