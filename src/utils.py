import json
import logging
import os

file_handler = logging.FileHandler(
    os.path.join(os.path.dirname(__file__), "..\\logs\\", "utils.log"), mode="w", encoding="utf-8"
)
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s %(lineno)d")
file_handler.setFormatter(file_formatter)


def load_operations(json_file_path):
    """Функция чтения объекта json из файла operations.json"""
    operations = []
    try:
if __name__ == "__main__":
    json_path = os.path.join(os.path.dirname(__file__), "..\\data\\", "operations.json")
    print(load_operations(json_path))
