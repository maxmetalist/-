def get_mask_card_number(card_number: str) -> str:
    """Функция маскирования номера карты"""

    if len(card_number) == 16 and card_number.isdigit():
        return card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
    else:
        return "Номер карты должен содержать 16 цифр"


print(get_mask_card_number("1234567812345678"))


def get_mask_account(account_number: str) -> str:
    """Функция маскирования номера счёта"""

    if len(account_number) == 20 and account_number.isdigit():
        return "**" + account_number[-4:]
    else:
        return "Номер счёта должен содержать 20 цифр"


print(get_mask_account("12345678123456781234"))