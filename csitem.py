class CsItem:
    def __init__(
            self,
            buff_min_price,
            steam_min_price,
            buff_max_order,
            steam_max_order,
            img_url,
            cs_item_name,
            buff_amount,
            buff_orders_amount,
            steam_amount,
            steam_orders_amount,
            item_id,
            steam_url
    ):
        self.buff_price = buff_min_price  # Минимальная цена, за которую предмет выставили на buff163
        self.steam_price = steam_min_price  # Минимальная цена, за которую предмет выставили на Steam
        self.buff_order = buff_max_order  # Максимальная цена ордера на buff163
        self.steam_order = steam_max_order  # Максимальная цена ордера на steam
        self.img_url = img_url  # URL-адрес картинки скина
        self.name = cs_item_name  # Полное имя скина
        self.buff_amount = buff_amount  # Кол-во предметов, выставленных на buff163
        self.buff_orders_amount = buff_orders_amount  # Кол-во ордеров, выставленных на предмет на buff163
        self.steam_amount = steam_amount  # Кол-во предметов, выставленных на steam
        self.steam_orders_amount = steam_orders_amount  # Кол-во ордеров, выставленных на предмет на steam
        self.id = item_id  # id предмета для получения ссылки goods
        self.steam_url = steam_url  # ссылка на предмет на steam

    def printitem(self):
        print(f"CSGO Item Printing...\n"
              f"Item name: \t{self.name}\n"
              f"BUFF163 Price: \t{self.buff_price}¥\n"
              f"BUFF163 Order: \t{self.buff_order}¥\n"
              f"Steam Price: \t{self.steam_price}$\n"
              f"Steam Order: \t{self.steam_order}$\n"
              f"Icon URL: \thttps://g.fp.ps.netease.com/market/file/{self.img_url}\n"
              f"Steam URL: \thttps://steamcommunity.com/market/listings/730/{self.steam_url}\n"
              f"Item url on buff: \t https://buff.163.com/goods/{self.id}?from=market#tab=selling"
              f"\nAmount (on BUFF163): \t{self.buff_amount}\n"
              f"Amount (on Steam): \t{self.steam_amount}\n"
              f"Order amount (on BUFF163): \t{self.buff_orders_amount}\n"
              f"Order amount (on Steam): \t{self.steam_orders_amount}\n")
        print('\n')
