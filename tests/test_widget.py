import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "value, expected",
    [
        ("", "Укажите тип 'счёт' или тип карты: Visa, Mastercard, МИР или иное"),
        ("1234567812345678", "Укажите тип 'счёт' или тип карты: Visa, Mastercard, МИР или иное"),
        ("visa electron 1234567812345678", "visa electron 1234 56** **** 5678"),
        ("счёт 12345678123456781234", "счёт **1234"),
        ("visa 1234567812345678", "visa 1234 56** **** 5678"),
        ("master card 1234567812345678", "master card 1234 56** **** 5678"),
        ("счёт 1234567812345678", "Тип 'счёт' должен содержать 20 цифр"),
    ],
)
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected


def test_get_date(date_revert_string, date_revert_empty, date_revert_notime):
    assert get_date("2024-03-11T02:26:18.671407") == date_revert_string
    assert get_date("") == date_revert_empty
    assert get_date("2022-05-22 15:34:14") == date_revert_notime
