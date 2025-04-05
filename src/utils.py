import json
import os


def load_operations(json_file_path):
    """Функция чтения объекта json из файла operations.json"""
    operations = []
    try:
        with open(json_file_path, "r", encoding="utf-8") as json_file:
            if not json_file:
                return operations
            else:
                operations = json.load(json_file)
                if type(operations) is not list:
                    return []
    except FileNotFoundError:
        print(f"Файл {json_file_path} не найден")
    except json.JSONDecodeError:
        print(f"Ошибка декодирования файла {json_file_path}")
    except Exception:
        print("Произошла ошибка")
    return operations


def open_file():
    """Функция, задающая путь к файлу"""
    json_file_path = os.path.join(os.path.dirname(os.getcwd()), "data", "operations.json")
    data_ = load_operations(json_file_path)
    return data_


if __name__ == "__main__":
    print(open_file())
