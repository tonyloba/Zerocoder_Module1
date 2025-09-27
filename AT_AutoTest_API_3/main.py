import requests

def get_random_cat_image():
    """
    Делает запрос к TheCatAPI и возвращает URL случайного изображения кошки.
    Если запрос неуспешен, возвращает None.
    """
    url = "https://api.thecatapi.com/v1/images/search"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data and isinstance(data, list) and "url" in data[0]:
                return data[0]["url"]
        return None
    except requests.RequestException:
        return None