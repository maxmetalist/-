def mask_account_card(card_type_number: str) -> str:
    """Функция для получения маски из номера карты или номера счёта"""
    alfa_text = ""
    digit_text = ""

    for symbol in card_type_number:
        if symbol.isalpha() or symbol == " ":
            alfa_text += symbol
        elif symbol.isdigit():
            digit_text += symbol

    if len(alfa_text) == 0:
        return "Укажите тип 'счёт' или тип карты: Visa, Mastercard, МИР или иное"

    if "счёт" in alfa_text and len(digit_text) == 20:
        return alfa_text + "**" + digit_text[-4:]
    elif "счёт" in alfa_text and len(digit_text) != 20:
        return "Тип 'счёт' должен содержать 20 цифр"
    elif len(digit_text) == 16:
        return alfa_text + digit_text[:4] + " " + digit_text[4:6] + "** **** " + digit_text[-4:]
    else:
        return "Некорректный номер карты или счёта.Номер карты должен иметь 16 цифр, номер счёта должен иметь 20 цифр."


# print(mask_account_card("visa 1234567812345678"))


def get_date(date: str) -> str:
    """Функция для вывода даты в формате дд.мм.гггг"""
    if len(date) != 0:
        new_date_list = date[:10].split("-")
        reversed_date_list = new_date_list[::-1]
        return ".".join(reversed_date_list)
    else:
        return "укажите дату в формате гггг-мм-дд"


# print(get_date("2024-03-11T02:26:18.671407"))
