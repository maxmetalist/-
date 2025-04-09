import os.path
from unittest.mock import mock_open, patch

import pandas as pd

from src.csv_xlsx_reader import read_csv_transactions, read_xlsx_transactions


def test_read_csv_transactions_wrong_path():
    """тест на корявый путь до csv файла csv"""
    transactions_csv_path = os.path.join("transactions.csv")
    result = read_csv_transactions(transactions_csv_path)
    assert result == []


def test_read_csv_transactions_correct():
    """Тест на нормальную работу функции по указанному пути"""
    transactions_csv_path = os.path.join(os.path.dirname(__file__), "..\\data\\", "transactions.csv")
    assert read_csv_transactions(transactions_csv_path)[0] == {
        "id": "650703",
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": "16210",
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
        "description": "Перевод организации",
    }


def test_read_csv_transactions():
    """Тест на нормальную работу функции с подменой данных"""
    transactions_path = os.path.join(os.path.dirname(__file__), "..\\data\\", "transactions.csv")
    mock_data = "id;state;date;amount;currency_name;currency_code;from;to;description\n1;2;3;4;5;6;7;8;9\n"
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = read_csv_transactions(transactions_path)
        assert result == [
            {
                "id": "1",
                "state": "2",
                "date": "3",
                "amount": "4",
                "currency_name": "5",
                "currency_code": "6",
                "from": "7",
                "to": "8",
                "description": "9",
            }
        ]


def test_read_csv_transactions_no_file():
    """Тест на ошибку при пустом или отсутствующем файле"""
    transactions_path = os.path.join(os.path.dirname(__file__), "..\\data\\", "transactions.csv")
    mock_data = ""
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = read_csv_transactions(transactions_path)
        assert result == []


def test_read_xlsx_transactions_wrong_path():
    transactions_xlsx_path = os.path.join("transactions_excel.xlsx")
    result = read_xlsx_transactions(transactions_xlsx_path)
    assert result == []


@patch("pandas.read_excel")
def test_read_xlsx_transactions_correct(mock_read_excel):
    """Тест на нормальную работу функции с подменой данных"""
    transactions_path = os.path.join(os.path.dirname(__file__), "..\\data\\", "transactions_excel.xlsx")
    mock_data = pd.DataFrame({"id": ["1", "2", "3"], "state": ["a", "b", "c"], "currency_name": ["d", "e", "f"]})
    mock_read_excel.return_value = mock_data
    result = read_xlsx_transactions(transactions_path)
    exp = [
        {"id": "1", "state": "a", "currency_name": "d"},
        {"id": "2", "state": "b", "currency_name": "e"},
        {"id": "3", "state": "c", "currency_name": "f"},
    ]
    assert result == exp


@patch("pandas.read_excel")
def test_read_xlsx_transactions_no_file(mock_read_excel):
    transactions_path = os.path.join(os.path.dirname(__file__), "..\\data\\", "transactions_excel.xlsx")
    mock_data = pd.DataFrame()
    mock_read_excel.return_value = mock_data
    result = read_xlsx_transactions(transactions_path)
    exp = []
    assert result == exp