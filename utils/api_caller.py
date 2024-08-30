import requests
from config import API_URL, HEADERS

def post_to_api(data, url=API_URL):
    response = requests.post(url, json=data, headers=HEADERS)
    return response.status_code, response.json()

