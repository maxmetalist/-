import os
import re
from collections import Counter

from src.csv_xlsx_reader import read_csv_transactions


def filter_by_user_string(transactions, user_string="организации"):
    """Функция фильтрации транзакций по описанию, заданному в строке(выводит данные о количестве
    заданных операций"""
    filtered_trans_list = []
    for transaction in transactions:
        if not transaction.get("description"):
            continue
        else:
            pattern = re.compile(user_string, re.IGNORECASE)
            filtered_transaction = pattern.search(transaction["description"])
            if filtered_transaction is not None:
                filtered_trans_list.append(transaction)
    return filtered_trans_list


if __name__ == "__main__":
    transactions_path = os.path.join(os.path.dirname(__file__), "..\\data\\", "transactions.csv")
    transactions_csv = read_csv_transactions(transactions_path)
    print(filter_by_user_string(transactions_csv, "вклад"))


def get_description_dict(transactions, descriptions):
    """функция подсчёта количества операций в каждой категории"""
    my_outer_dict = {}
    description_list = []
    for transaction in transactions:
        if transaction.get("description"):
            description_list.append(transaction["description"])
    counter = Counter(description_list)
    for key, value in counter.items():
        if key.lower() in descriptions:
            my_outer_dict[key] = value

    return my_outer_dict


transactions_path = os.path.join(os.path.dirname(__file__), "..\\data\\", "transactions.csv")
transactions_csv = read_csv_transactions(transactions_path)
string = "перевод с карты на карту,перевод организации,открытие вклада"
descriptions_list = string.split(",")
print(get_description_dict(transactions_csv, descriptions_list))
