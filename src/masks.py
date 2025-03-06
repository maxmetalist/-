def get_mask_card_number(card_number: str) -> str:
    """Функция маскирования номера карты"""
    return card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]


print(get_mask_card_number(str(input("Введите номер карты"))))


def get_mask_account(account_number: str) -> str:
    """Функция маскирования номера счёта"""
    return "**" + account_number[-4:]


print(get_mask_account(str(input("Введите номер счёта"))))
