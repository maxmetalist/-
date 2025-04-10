import logging
import os

file_handler = logging.FileHandler(
    os.path.join(os.path.dirname(__file__), "..\\logs\\", "masks.log"), mode="w", encoding="utf-8"
)
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s %(lineno)d")
file_handler.setFormatter(file_formatter)


def get_mask_card_number(card_number: str) -> str:
    """Функция маскирования номера карты"""
        return "Номер карты должен содержать 16 цифр"


print(get_mask_card_number("1234567812345678"))


def get_mask_account(account_number: str) -> str:
    """Функция маскирования номера счёта"""
        return "Номер счёта должен содержать 20 цифр"


print(get_mask_account("12345678123456781234"))
