import pytest


@pytest.fixture
def date_revert_string():
    """Фикстура для функции преоразования даты на корректность вывода"""
    return "11.03.2024"


@pytest.fixture
def date_revert_empty():
    """Фикстура для функции преобразования даты на пустую строку"""
    return "укажите дату в формате гггг-мм-дд"


@pytest.fixture
def date_revert_notime():
    return "22.05.2022"


@pytest.fixture
def filter_by_currency_empty():
    return "Нет транзакций в данной валюте"


@pytest.fixture
def transaction_descriptions_empty():
    return "Нет данных транзакции"


@pytest.fixture
def transaction_no_descriptions():
    return "Нет данных транзакции"


@pytest.fixture
def convert_amount_rub():
    return "200.0"


@pytest.fixture
def convert_amount_no_curr():
    return "Укажите валюту"


@pytest.fixture
def convert_amount_no_amount():
    return "Укажите сумму для конвертации"