import requests
from bs4 import BeautifulSoup

def get_date_and_check_date(input_date: str) -> tuple:
    "Получение данных с сайта и проверка их соответствия запрошенной дате"
    try:
        r = requests.get(f'https://cbr.ru/currency_base/daily/?UniDbQuery.Posted=True&UniDbQuery.To={input_date}')
    except:
        return "Сайт не доступен", True
    soup = BeautifulSoup(r.text, features="html.parser")
    date_from_site = soup.find("button", "datepicker-filter_button")
    if date_from_site.text == input_date:
        return soup, None
    else:
        return "За указанную дату курсов нет", True


def get_curr_date(block_with_date: BeautifulSoup, selected_curr: str) -> str:
    for elem in block_with_date.findAll("tr"):
        curr_block = elem.findAll("td")
        if (len(curr_block)) >0 and curr_block[1].text == selected_curr:
            return  f"Курс за {curr_block[2].text} {curr_block[3].text} равен {curr_block[4].text} рублей"
    return  "Такой валюты на сайте нет"


def make_magic(input_date: str, selected_curr: str) -> str:
    "Главная функция, отвечающая за работу остальных функций"
    res, err = get_date_and_check_date(input_date)
    if not err:
        final_result = get_curr_date(res, selected_curr)
        return final_result
    else:
        return res




