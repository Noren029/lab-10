import requests
import os
from PIL import Image

def get_pokemon_list():
    url = "https://pokeapi.co/api/v2/pokemon?limit=50"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return [pokemon['name'].capitalize() for pokemon in data['results']]
    return []

def get_pokemon_info(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def download_pokemon_image(pokemon_name, save_dir="images"):
    os.makedirs(save_dir, exist_ok=True)
    image_path = os.path.join(save_dir, f"{pokemon_name}.png")
    
    pokemon_info = get_pokemon_info(pokemon_name)
    if pokemon_info:
        image_url = pokemon_info["sprites"]["other"]["official-artwork"]["front_default"]
        if image_url:
            response = requests.get(image_url, stream=True)
            if response.status_code == 200:
                with open(image_path, 'wb') as file:
                    for chunk in response.iter_content(1024):
                        file.write(chunk)
                return image_path
    return None

