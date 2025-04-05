import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def convert_amount(transact):
    """Функция конвертации валюты"""
    if transact == {} or transact.get("operationAmount").get("currency").get("code") == "":
        return "Укажите валюту"
    elif not transact.get("operationAmount").get("amount"):
        return "Укажите сумму для конвертации"
    else:
        value = transact["operationAmount"]["amount"]
        from_ = transact["operationAmount"]["currency"]["code"]
        to = "RUB"
        try:
            if transact["operationAmount"]["currency"]["code"] == "RUB":
                return str(value)
            else:
                url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_}&amount={value}"
                headers = {"apikey": API_KEY}
                response = requests.get(url, headers=headers)
                status_code = response.status_code
                result = response.json()["result"]
                if status_code == 200:
                    return result
                else:
                    return "Запрос отклонён. Причина: некорректные данные"
        except requests.exceptions.RequestException:
            print("Произошла ошибка. Проверьте корректность данных")


if __name__ == "__main__":
    transaction = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": 100.00, "currency": {"name": "USD", "code": "USD"}},
    }
    print(convert_amount(transaction))