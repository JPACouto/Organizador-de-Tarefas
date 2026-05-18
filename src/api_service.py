import requests


def get_motivational_quote():
    url = "https://api.adviceslip.com/advice"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        data = response.json()

        return {
            "content": data["slip"]["advice"],
            "author": "Advice Slip API",
        }

    except requests.RequestException:
        return {
            "content": "Não foi possível carregar a frase.",
            "author": "Sistema",
        }