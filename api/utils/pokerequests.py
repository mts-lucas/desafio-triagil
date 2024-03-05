import requests

def do_requests(string_list):
    erros = []
    pkmns = []
    url = "https://pokeapi.co/api/v2/pokemon"
    for string in string_list:
        string_lower: str = string.lower()
        myurl = f"{url}/{string_lower}"
        response = requests.get(myurl)
        if response.status_code != 200:
            erros.append(f"Pokemon de nome:{string}, nao foi encontrado em pokeapi.co")
        else:
            pkmns.append(response.json())
    return erros, pkmns
