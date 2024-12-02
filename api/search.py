import requests

API_KEY = "AIzaSyBmjRNwNBNY1A6g6Qfv9aUBV_rD1Zz03lw"  # Укажите ваш Google API ключ
CX = "1277afbc49d06402d"  # Создайте его в Google Custom Search JSON API

def perform_search(query, search_type="standard"):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {"key": API_KEY, "cx": CX, "q": query}

    if search_type == "time":
        params["sort"] = "date:r:week"
    elif search_type == "site":
        params["q"] += f" site:{query.split()[-1]}"

    response = requests.get(url, params=params)
    return response.json().get("items", [])
