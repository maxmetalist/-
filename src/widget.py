def mask_account_card(card_type_number: str) -> str:
    """Функция для получения маски из номера карты или номера счёта"""
    alfa_text = ""
    digit_text = ""

    for symbol in card_type_number:
        if symbol.isalpha():
            alfa_text += symbol
        else:
            digit_text += symbol

    if "Счёт" in alfa_text:
        return alfa_text + "**" + digit_text[-4:]
    else:
        return alfa_text + digit_text[:4] + " " + digit_text[4:6] + "** **** " + digit_text[-4:]


print(mask_account_card(str(input("Введите номер и тип карты или счёта"))))


def get_date(date: str) -> str:
    """Функция для вывода даты в формате дд.мм.гггг"""
    new_date_list = date[:10].split("-")
    reversed_date_list = new_date_list[::-1]
    return ".".join(reversed_date_list)


print(get_date("2024-03-11T02:26:18.671407"))
