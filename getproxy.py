import requests
from bs4 import BeautifulSoup as Bs4

def get_proxy():
    url = "https://free-proxy-list.net/"
    proxies_response = requests.get(url)
    soup = Bs4(proxies_response.text)
    soup.find()
