import pytest

from src.utils import executed_operations, sort_date


@pytest.fixture
def date():
    return [{'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08T22:46:21.935582',
             'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}},
             'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'},
            {'id': 482520625, 'state': 'EXECUTED', 'date': '2019-11-13T17:38:04.800051',
             'operationAmount': {'amount': '62814.53', 'currency': {'name': 'руб.', 'code': 'RUB'}},
             'description': 'Перевод со счета на счет', 'from': 'Счет 38611439522855669794',
             'to': 'Счет 46765464282437878125'}]


def test_executed_operations(date):
    assert len(executed_operations(date)) == 2


def test_sort_date(date):
    assert len(sort_date(date)) == 2
