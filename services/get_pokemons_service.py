import requests


def get_pokemons():
    url = 'https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0'
    resp = requests.get(url)

    return resp.json()['results']

pokemons = get_pokemons()

print(pokemons, type(pokemons))
