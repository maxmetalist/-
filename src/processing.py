from typing import Union


def filter_by_state(id_list: list, state: str = "EXECUTED") -> Union[list, str]:
    """Функция фильтрации транзакций по параметру состояния"""
    filtered_list = []

    if not id_list:
        return "Укажите данные транзакции: id клиента, состояние, дата"
    else:
        for id_number in id_list:
            if id_number.get("state", 0) == "":
                return "Параметр состояния отсутствует или находится в состоянии CANCELED"
            elif id_number.get("state", 0) == state:
                filtered_list.append(id_number)
        return filtered_list


print(
    filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)


def sort_by_date(id_list: list, reverse: bool = True) -> list:
    """Функция сортировки по дате"""

    if not id_list:
        return list("Укажите данные транзакции: id клиента, состояние, дата")
    else:
        sorted_list = sorted(id_list, key=lambda x: x["date"], reverse=reverse)
        return sorted_list


print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-11-14T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)
