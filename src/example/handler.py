import json
import os
import base64
import requests

from src.lib import config as _config


def run(*args, **kwargs):
    apaleo_id = _config.get_config().get(['APALEO_ID'])
    return get_access_token(apaleo_id)


def get_access_token(apaleo_id):
    '''
    Get the Apaleo Access token for the provided apaleo id
    :param apaleo_id: The apaleo account id
    :return: The access token for future Apaleo API calls
    '''
    credentials = base64.standard_b64encode(apaleo_id.encode('utf-8'))
    credentials = str(credentials, 'utf-8')
    data = 'grant_type=client_credentials'
    headers = {
        'content-type': 'application/x-www-form-urlencoded',
        'Authorization': 'Basic {}'.format(credentials)
    }
    url = 'https://identity.apaleo.com/connect/token'
    request = requests.post(url=url, data=data, headers=headers)
    return request.json()['access_token']