import logging
import os

logger_masks = logging.getLogger("masks")
file_handler = logging.FileHandler(
    os.path.join(os.path.dirname(__file__), "..\\logs\\", "masks.log"), mode="w", encoding="utf-8"
)
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s %(lineno)d")
file_handler.setFormatter(file_formatter)
logger_masks.addHandler(file_handler)
logger_masks.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """Функция маскирования номера карты"""
    logger_masks.debug("Проверка формата номера карты для создания маски")
    if len(card_number) == 16 and card_number.isdigit():
        logger_masks.debug("Вывод результата")
        return card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
    else:
        logger_masks.error("Не верный формат номера карты")
        return "Номер карты должен содержать 16 цифр"


print(get_mask_card_number("1234567812345678"))


def get_mask_account(account_number: str) -> str:
    """Функция маскирования номера счёта"""
    logger_masks.debug("Проверка формата номера счёта для создания маски")
    if len(account_number) == 20 and account_number.isdigit():
        logger_masks.debug("Вывод результата")
        return "**" + account_number[-4:]
    else:
        logger_masks.error("Не верный формат номера счёта")
        return "Номер счёта должен содержать 20 цифр"


print(get_mask_account("12345678123456781234"))
