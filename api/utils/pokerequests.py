import requests

def do_requests(string_list):
    erros = []
    pkmns = []
    url = "https://pokeapi.co/api/v2/pokemon"
    for string in string_list:
        url = f"{url}/{string}"
        response = requests.get(url)
        if response.status_code != 200:
            erros.append(f"Pokemon de nome:{string}, nao foi encontrado em pokeapi.co")
        else:
            pkmns.append(response.json())
    return erros, pkmns
