import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    "value, expected",
    [
        ("1234567812345678", "1234 56** **** 5678"),
        ("12345678", "Номер карты должен содержать 16 цифр"),
        ("asdf1234", "Номер карты должен содержать 16 цифр"),
        ("12345678123456781234", "Номер карты должен содержать 16 цифр"),
        ("", "Номер карты должен содержать 16 цифр"),
    ],
)
def test_get_mask_card_number(value, expected):
    """Тест на функцию маскирования номера карты"""
    assert get_mask_card_number(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        ("1234567812345678", "Номер счёта должен содержать 20 цифр"),
        ("12345678", "Номер счёта должен содержать 20 цифр"),
        ("asdf1234", "Номер счёта должен содержать 20 цифр"),
        ("12345678123456781234", "**1234"),
        ("", "Номер счёта должен содержать 20 цифр"),
    ],
)
def test_get_mask_account(value, expected):
    """Тест на функцию маскирования номера счёта"""
    assert get_mask_account(value) == expected