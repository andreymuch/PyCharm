"""
проект парсит цены на товары из ряда магазинов и цену доставки, после чегообновляет(вносит) данные в базу данных
обновляет данные каждый день
показывает итоговую минимальную сумму заказа
телеграм бот
"""

import bs4, lxml
import requests
from parserdb import Database


class Parser(object):
    def __init__(self):
        self.shops_pages = [
            "https://www.perekrestok.ru/cat"
        ]
        self.headers = {
            "Accept": "* / *",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                      " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
        }

        self.db = Database()
        self.db.delete_from_db(())
        for i in range(len(self.shops_pages)):
            html_text = requests.get(self.shops_pages[i], self.headers).text
            self.soup = bs4.BeautifulSoup(html_text, "lxml")  # полученный код штмл странички
            cat = self.soup.findAll("a", class_="sc-jSgupP bnmesn")
            for j in cat:
                second_part = self.shops_pages[i][0:-4] + str(j.get("href"))
                html_text_cat = requests.get(second_part, self.headers).text
                self.soup_cat = bs4.BeautifulSoup(html_text_cat, "lxml")
                self.find_costs(self.soup_cat)

    def find_costs(self, product_href) -> None:
        product_name = product_href.findAll("div", class_="product-card__title")
        product_cost = product_href.findAll("div", class_="price-new")
        for name in range(len(product_name)):
            cost = ""
            for i in product_cost[name].text:
                if i.isdigit() or i == ",":
                    if i == ",":
                        cost += "."
                    else:
                        cost += i
            try:
                self.db.append_data_base((product_name[name].text.strip().replace("'", "`"), float(cost)))
            except Exception as ex:
                print("error in database.............")
                print(ex)


if __name__ == "__main__":
    parser = Parser()

