import requests
from data import headers_post_auth
from data import headers


def get_page():
    for page in range(2, 11):
        url = f"https://buff.163.com/api/market/goods?game=csgo&page_num={page}&use_suggestion=0&_=1672932038531"
        buff_session = requests.Session()
        login_response = buff_session.post(url='https://buff.163.com/account/api/user/info?_=1673003802570',
                                           headers=headers_post_auth)
        if login_response:
            print("Login error. Check Cookies in datas.py/headers_post_auth\n")
            exit()
        market_response = buff_session.get(url, headers=headers).json()
        yield market_response

#   Генератор возвращает страницу в виде response
