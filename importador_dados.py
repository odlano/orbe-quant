

import requests

API_KEY = "123"
BASE_URL = f"https://www.thesportsdb.com/api/v1/json/{API_KEY}"

def importar_ligas_futebol():
    url = f"{BASE_URL}/search_all_leagues.php"
    parametros = {"s": "Soccer"}

    resposta = requests.get(url, params=parametros, timeout=20)
    resposta.raise_for_status()

    dados = resposta.json()
    ligas = dados.get("leagues") or []

    print(f"Total de ligas encontradas: {len(ligas)}")

    for liga in ligas:
        print({
            "nome": liga.get("strLeague"),
            "esporte": liga.get("strSport"),
            "pais": liga.get("strCountry")
        })

    return ligas


if __name__ == "__main__":
    importar_ligas_futebol()
