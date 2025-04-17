import os

from src.csv_xlsx_reader import read_csv_transactions, read_xlsx_transactions
from src.filters import filter_by_user_string
from src.generators import filter_by_currency
from src.processing import sort_by_date
from src.utils import load_operations


def main():
    """главная функция обработки списка транзакций по запросу пользователя"""
    print(
        "Привет! Добро пожаловать в программу работы с банковскими транзакциями."
        "\nВыберите необходимый путь меню (введите соответствующую цифру):"
        "\n1: Получить информацию из JSON файла"
        "\n2: Получить информацию из CSV файла"
        "\n3: Получить информацию из XLSX файла"
    )

    while True:
        # цикл выборки исходного файла
        user_input_file = input().lower().strip()
        if user_input_file.isdigit():
            if user_input_file == "1":
                print("Для обработки выбран JSON файл")
                json_path = os.path.join(os.path.dirname(__file__), "..\\data\\", "operations.json")
                transactions = load_operations(json_path)
                result = []
                for transaction in transactions:
                    transformed = {
                        "id": transaction.get("id", ""),
                        "state": transaction.get("state", ""),
                        "date": transaction.get("date", ""),
                        "amount": transaction.get("operationAmount", {}).get("amount", ""),
                        "currency_name": transaction.get("operationAmount", {}).get("currency", {}).get("name", ""),
                        "currency_code": transaction.get("operationAmount", {}).get("currency", {}).get("code", ""),
                        "description": transaction.get("description", ""),
                        "from": transaction.get("from", ""),
                        "to": transaction.get("to", ""),
                    }
                    result.append(transformed)
                transactions_list = result

                break
            elif user_input_file == "2":
                print("Для обработки выбран CSV файл")
                transactions_path = os.path.join(os.path.dirname(__file__), "..\\data\\", "transactions.csv")
                transactions_list = read_csv_transactions(transactions_path)
                break
            elif user_input_file == "3":
                print("Для обработки выбран XLSX файл")
                transactions_path = os.path.join(os.path.dirname(__file__), "..\\data\\", "transactions_excel.xlsx")
                transactions_list = read_xlsx_transactions(transactions_path)
                break
            print('Введите "1", "2" или "3"')

    print(
        "Введите статус, по которому необходимо провести фильтрацию."
        "\nДоступные статусы: EXECUTED "
        "\nCANCELED "
        "\nPENDING "
    )

    while True:
        # цикл сортировки по состоянию
        user_input_state = input().upper().strip()
        if user_input_state == "EXECUTED" or user_input_state == "CANCELED" or user_input_state == "PENDING":
            print(f"Выбрана фильтрация по статусу {user_input_state}")
            break
        print("Некорректный статус. Введите один из трёх доступных:" "\nEXECUTED" "\nCANCELED" "\nPENDING")
    if not transactions_list:
        print("Нет списка транзакций")
    else:
        filtered_transactions_list = [
            transaction for transaction in transactions_list if transaction.get("state") == user_input_state
        ]

    while True:
        # цикл сортировки по дате
        user_input_date = input("Сортировать по дате? Введите Да/Нет ").lower().strip()
        if user_input_date == "да":
            while True:
                # вложенный цикл сортировки по возрастанию\убыванию
                user_input_reverse_date = (
                    input(
                        "Сортировать по возрастанию/убыванию" "\nПо возрастанию введите 1 " "\nПо убыванию введите 2 "
                    )
                    .lower()
                    .strip()
                )
                if user_input_reverse_date == "1":
                    filtered_transactions_list_by_date = sort_by_date(filtered_transactions_list, reverse=True)
                    break
                elif user_input_reverse_date == "2":
                    filtered_transactions_list_by_date = sort_by_date(filtered_transactions_list, reverse=False)
                    break
                # return filtered_transactions_list_by_date
            break
        elif user_input_date == "нет":
            filtered_transactions_list_by_date = filtered_transactions_list
            break
    # return filtered_transactions_list_by_date

    while True:
        # цикл сортировки по валюте
        user_input_currency = input("Выводить только рублёвые транзакции? Введите Да/Нет ").lower().strip()

        if user_input_currency == "да":
            filtered_by_currency = list(filter_by_currency(filtered_transactions_list_by_date, "RUB"))
            break
        elif user_input_currency == "нет":
            filtered_by_currency = filtered_transactions_list_by_date
            break
    # return filtered_by_currency

    while True:
        # цикл сортировки по слову в описании
        user_input_word = input("Сортировать по определённому слову в описании? Введите Да/Нет ").lower().strip()
        if user_input_word == "да":
            user_input_word_yes = input("Введите слово, например 'вклад' или 'перевод' ")
            outer_filtered_list = filter_by_user_string(filtered_by_currency, user_input_word_yes)
            break
        elif user_input_word == "нет":
            outer_filtered_list = filtered_by_currency
            break
    if not outer_filtered_list:
        return "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
    else:
        return outer_filtered_list


if __name__ == "__main__":
    print(main())
