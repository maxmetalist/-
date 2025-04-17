from src.generators import (card_number_generator, filter_by_currency, transaction_descriptions, transactions,
                            transactions_empty, transactions_no_description)


def test_filter_by_currency_usd():
    """тест на корректность при валидных данных и корректное завершение"""
    generator = filter_by_currency(transactions, "USD")
    try:
        assert next(generator) == {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "amount": "9824.07",
            "currency_name": "USD",
            "currency_code": "USD",
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        }
        assert next(generator) == {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "amount": "79114.93",
            "currency_name": "USD",
            "currency_code": "USD",
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        }
        assert next(generator) == {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "amount": "56883.54",
            "currency_name": "USD",
            "currency_code": "USD",
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        }
    except StopIteration:
        assert next(generator) == "Нет транзакций в данной валюте"


def test_filter_by_currency_rub():
    """тест на корректность при условии фильтрации по рублям"""
    generator = filter_by_currency(transactions, "RUB")
    try:
        assert next(generator) == {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "amount": "43318.34",
            "currency_name": "руб.",
            "currency_code": "RUB",
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        }
        assert next(generator) == {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "amount": "67314.70",
            "currency_name": "руб.",
            "currency_code": "RUB",
            "description": "Перевод от организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        }
    except StopIteration:
        assert next(generator) == "Нет транзакций в данной валюте"


def test_filter_by_currency(filter_by_currency_empty):
    generator = filter_by_currency(transactions_empty)
    try:
        next(generator)
    except StopIteration:
        assert "Нет транзакций в данной валюте" == filter_by_currency_empty


def test_transaction_descriptions():
    gen = transaction_descriptions(transactions)
    try:
        assert next(gen) == "Перевод организации"
        assert next(gen) == "Перевод со счета на счет"
        assert next(gen) == "Перевод со счета на счет"
        assert next(gen) == "Перевод с карты на карту"
        assert next(gen) == "Перевод от организации"
    except StopIteration:
        assert next(gen) == "Нет данных транзакции"


def test_transaction_descriptions_empty(transaction_descriptions_empty):
    generator = transaction_descriptions(transactions_empty)
    try:
        next(generator)
    except StopIteration:
        assert "Нет данных транзакции" == transaction_descriptions_empty


def test_transaction_descriptions_no_descriptions(transaction_no_descriptions):
    generator = transaction_descriptions(transactions_no_description)
    try:
        next(generator)
    except StopIteration:
        assert "Нет данных транзакции" == transaction_no_descriptions


def test_card_number_generator():
    generator = card_number_generator(1, 5)
    try:
        assert next(generator) == "0000 0000 0000 0001"
        assert next(generator) == "0000 0000 0000 0002"
        assert next(generator) == "0000 0000 0000 0003"
        assert next(generator) == "0000 0000 0000 0004"
    except StopIteration:
        assert next(generator) == "0000 0000 0000 0005"
        assert next(generator) == "В этом диапазоне уже существуют номера карт. Укажите другой диапазон"


def test_card_number_generator_():
    generator = card_number_generator(9999999999999997, 9999999999999999)
    try:
        assert next(generator) == "9999 9999 9999 9997"
        assert next(generator) == "9999 9999 9999 9998"
    except StopIteration:
        assert next(generator) == "9999 9999 9999 9999"
