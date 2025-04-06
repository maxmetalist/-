import json
import os
import tempfile
from unittest.mock import patch

from src.utils import load_operations


def test_load_operations_wrong_path():
    """Проверка на неправильный путь"""
    json_file = os.path.join("src", "operations.json")
    result = load_operations(json_file)
    assert result == []


@patch("json.load")
def test_load_operations_decode_err(mock_json):
    """Проверка на ошибку декодирования"""
    mock_json.side_effect = json.decoder.JSONDecodeError("", "data/operations.json", 1)

    assert load_operations("data/operations.json") == []


def test_load_operations_invalid_content():
    """Проверка на некорректное содержимое(не список)"""
    test_data = {"key": "value"}
    tmp_path = tempfile.mktemp(suffix=".json")
    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump(test_data, f)
    result = load_operations(tmp_path)
    assert result == []

    if os.path.exists(tmp_path):
        os.remove(tmp_path)


def test_load_operations_correct():
    """Проверка на корректное завершение"""
    json_file = os.path.join(os.path.dirname(os.getcwd()), "data", "operations.json")
    datas = load_operations(json_file)
    assert load_operations(json_file) == datas
