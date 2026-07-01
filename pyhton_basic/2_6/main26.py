#requesting API

import requests

base_url = "https://pokeapi.co/api/v2/pokemon/"

def get_pokemon_data(pokemon_name):
    url = base_url + pokemon_name.lower()
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print("Pokémon Data:")
        print(f"Name: {data['name']}")
        print(f"Height: {data['height']}")
        print(f"Weight: {data['weight']}")
    else:
        print("Failed to retrieve data. Status code:", response.status_code)

pokemon_name = input("Enter the name of a Pokémon: ")
get_pokemon_data(pokemon_name)