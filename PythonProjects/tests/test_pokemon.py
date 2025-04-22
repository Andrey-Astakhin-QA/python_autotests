import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'fba1f09d6107e6d8aeb1f1b272325c69'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '31187'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["id"] == TRAINER_ID    

@pytest.mark.parametrize('key, value', [('id', TRAINER_ID), ('trainer_name', 'Андрей'), ('level', '5')])
def test_parametrize (key, value):
    response_parametrize = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value