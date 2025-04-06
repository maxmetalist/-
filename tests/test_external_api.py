from unittest.mock import patch

from src.external_api import convert_amount


def test_convert_amount_rub(convert_amount_rub):
    transaction_test = {"operationAmount": {"amount": 200.00, "currency": {"code": "RUB"}}}
    assert convert_amount(transaction_test) == convert_amount_rub


@patch("src.external_api.requests.get")
def test_convert_amount_usd(mock_request):
    transaction_test = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": 100.00, "currency": {"name": "USD", "code": "USD"}},
    }

    mock_request.return_value.status_code = 200
    mock_request.return_value.json.return_value = {"result": 8515.5447, "success": "true"}
    result = convert_amount(transaction_test)
    assert result == 8515.5447


@patch("src.external_api.requests.get")
def test_convert_amount_incorrect_req(mock_request):
    transaction_test = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": 100.00, "currency": {"name": "USD", "code": "USD"}},
    }
    mock_request.return_value.json.return_value = {"result": 8515.5447, "success": "true"}
    result = convert_amount(transaction_test)
    assert result == "Запрос отклонён. Причина: некорректные данные"


def test_convert_amount_no_transact(convert_amount_no_curr):
    transaction_test = {}
    assert convert_amount(transaction_test) == convert_amount_no_curr


def test_convert_amount_no_amount(convert_amount_no_amount):
    transaction_test = {"operationAmount": {"currency": {"code": "RUB"}}}
    assert convert_amount(transaction_test) == convert_amount_no_amount
