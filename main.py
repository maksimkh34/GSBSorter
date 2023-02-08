from buffmodules import get_page
import requests
from data import headers
from bs4 import BeautifulSoup as Bs4
from csitem import CsItem
from urlcroppers import *

for page in get_page():
    try:
        items = page['data']['items']
    except Exception:
        print("Page is empty. Check login or connection...\n")
        exit(0)  # У buff бывают проблемы с входом. Поэтому, если страница не загрузилась 
        # (а грузится она только если зайти в аккаунт), 
        # программа завершится.

    for skin in items:
        item_url = skin['steam_market_url']
        response = requests.get(item_url, headers=headers)

        # Получили URL предмета на тп Steam

        soup = Bs4(response.text, "lxml")
        data = soup.find_all("script", type="text/javascript")
        new_data = str(data[-1].text)  # Фильтрование данных скина

        index = new_data.find("Market_LoadOrderSpread")
        _ids = new_data[index:index + 35]
        ids = _ids.split(' ')
        item_id = ids[1]

        # Получили id скина для работы с ним на тп Steam

        scriptUrl = f"https://steamcommunity.com/market/itemordershistogram?country=EN"
        scriptUrl += f"&language=russian&currency=1"
        scriptUrl += f"&item_nameid={item_id}&two_factor=0"

        # Формирование ссылки на тп Steam

        steam_price_session = requests.Session()
        steam_price_response = steam_price_session.get(scriptUrl, headers=headers).json()
        steam_min_price = steam_price_response['lowest_sell_order']
        steam_max_order = steam_price_response['highest_buy_order']

        steam_min_price = steam_min_price[:-2] + '.' + steam_min_price[-2:]
        steam_max_order = steam_max_order[:-2] + '.' + steam_max_order[-2:]

        steam_orders_total = steam_price_response['buy_order_graph'][0][1]

        steam_sells_total = str(steam_price_response['sell_order_summary'])
        start_index_sells_total = steam_sells_total.find('orders_header_promote">')
        end_index_sells_total = steam_sells_total.find('</span><br>')
        steam_sells_total = steam_sells_total[start_index_sells_total + 23:end_index_sells_total]

        # Сбор остальных данных предмета

        new_item = CsItem(
            skin['sell_min_price'],
            steam_min_price,
            skin['buy_max_price'],
            steam_max_order,
            img_url_crop(skin['goods_info']['icon_url']),
            skin['market_hash_name'],
            skin['sell_num'],
            skin['buy_num'],
            steam_sells_total,
            steam_orders_total,
            skin['id'],
            steam_url_crop(skin['steam_market_url'])
        )
        new_item.printitem()
