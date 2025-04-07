import json
import logging
import os

logger_utils = logging.getLogger("utils")
file_handler = logging.FileHandler(
    os.path.join(os.path.dirname(__file__), "..\\logs\\", "utils.log"), mode="w", encoding="utf-8"
)
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s %(lineno)d")
file_handler.setFormatter(file_formatter)
logger_utils.addHandler(file_handler)
logger_utils.setLevel(logging.DEBUG)


def load_operations(json_file_path):
    """Функция чтения объекта json из файла operations.json"""
    operations = []
    try:
        logger_utils.debug("Запрос на чтение файла")
        with open(json_file_path, "r", encoding="utf-8") as json_file:
            if not json_file:
                logger_utils.error("Файл не существует или пустой")
                logger_utils.error("Результат: []")
                return operations
            else:
                logger_utils.debug("Декодирование файла в python-объект")
                operations = json.load(json_file)
                if type(operations) is not list:
                    logger_utils.error("Файл находится не в формате списка")
                    logger_utils.error("Результат: []")
                    return []
    except FileNotFoundError:
        logger_utils.error("Файл по указанному пути не найден")
        # print(f"Файл {json_file_path} не найден")
    except json.JSONDecodeError:
        logger_utils.error("Ошибка декодирования")
        # print(f"Ошибка декодирования файла {json_file_path}")
    except Exception as e:
        logger_utils.error(f"Ошибка {e}")
        # print(f"Произошла ошибка: {e}")
    logger_utils.debug("Вывод результата")
    return operations


def open_file():
    """Функция, задающая путь к файлу"""
    json_file_path = os.path.join(os.path.dirname(__file__), "..\\data\\", "operations.json")
    data_ = load_operations(json_file_path)
    return data_


if __name__ == "__main__":
    print(open_file())
