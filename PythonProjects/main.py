import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'fba1f09d6107e6d8aeb1f1b272325c69'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
body_create = {
    "name": "Бульба",
    "photo_id": 12
}
body_rename = {
    "pokemon_id": "298208",
    "name": "Bulba",
    "photo_id": 14
}
body_add_pokeball = {
    "pokemon_id": "298208"
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''response_rename = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_rename)
print(response_rename.text)'''

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)
