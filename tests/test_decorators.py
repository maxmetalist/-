import os
import tempfile

import pytest

from src.decorators import log


def test_log():
    """тест внутренней функции декоратора на различные параметры"""

    @log(filename="mylog.txt")
    def summ_(x, y):
        return x + y

    result_sum = summ_(1, 2)
    assert result_sum == 3

    def sub_(x, y):
        return x - y

    result_sub = sub_(2, 1)
    assert result_sub == 1

    def division_corr(x, y):
        return x / y

    result_div_corr = division_corr(4, 2)
    assert result_div_corr == 2

    def division_zero(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        division_zero(2, 0)


def test_my_function_error(capsys):
    """тест декоратора на вывод в консоль при выходе исключения"""

    @log()
    def my_function(x, y):
        return x / y

    my_function(2, 0)
    captured = capsys.readouterr()
    assert captured.out == "my_function error: division by zero. Inputs: (2, 0), {}\n"


def test_my_function_correct(capsys):
    """тест декоратора на вывод в консоль при удачном завершении функции"""

    @log()
    def my_function(x, y):
        return x / y

    my_function(4, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok. Res: 2.0\n"


with tempfile.NamedTemporaryFile(delete=False) as temp_file:
    temp_filename = temp_file.name


@log(filename=temp_filename)
def test_function():
    """тест для проверки записи лога в файл"""
    x = 1
    y = 2
    return x / y


try:
    test_function()
finally:
    with open(temp_filename, "r") as file:
        log_content = file.read()
        assert "test_function ok. Res: 0.5" in log_content

    os.remove(temp_filename)


@log(filename=temp_filename)
def test_function():
    """тест для проверки записи лога в файл"""
    x = 1
    y = 0
    return x / y


try:
    test_function()
finally:
    with open(temp_filename, "r") as file:
        log_content = file.read()
        assert "test_function error: division by zero. Inputs: (), {}" in log_content

    os.remove(temp_filename)
