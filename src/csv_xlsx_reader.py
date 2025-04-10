import csv
import os.path

import pandas as pd


def read_csv_transactions(transactions_csv_path):
    """Функция, открывающая файл csv по указанному пути и выдающая список словарей с транзакциями"""
    transactions_list_csv = []
    try:
        with open(transactions_csv_path, "r", encoding="utf-8") as file_csv:
            reader = csv.DictReader(file_csv, delimiter=";")
            for row in reader:
                row_dict = {
                    "id": row["id"],
                    "state": row["state"],
                    "date": row["date"],
                    "amount": row["amount"],
                    "currency_name": row["currency_name"],
                    "currency_code": row["currency_code"],
                    "from": row["from"],
                    "to": row["to"],
                    "description": row["description"],
                }
                transactions_list_csv.append(row_dict)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    return transactions_list_csv


if __name__ == "__main__":
    transactions_path = os.path.join(os.path.dirname(__file__), "..\\data\\", "transactions.csv")
    print(read_csv_transactions(transactions_path))


def read_xlsx_transactions(transactions_xlsx_path):
    """Функция, считывающая файл excel по указанному пути"""
    transactions_list_xlsx = []
    try:
        data_frame = pd.read_excel(transactions_xlsx_path, dtype=str, engine="openpyxl")
        transactions_list_xlsx = data_frame.to_dict(orient="records")
    except Exception as ex:
        print(f"Произошла ошибка {ex}")
    return transactions_list_xlsx


if __name__ == "__main__":
    transactions_path = os.path.join(os.path.dirname(__file__), "..\\data\\", "transactions_excel.xlsx")
    print(read_xlsx_transactions(transactions_path))
