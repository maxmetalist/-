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