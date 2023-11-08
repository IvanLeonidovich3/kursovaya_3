import json
from typing import Any


#  14.10.2018
def load_operation():
    """загружает список операций"""
    with open('operations.json', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data  # список всех операций из json файла


def sort_date(date: Any) -> list:
    """сортирует список операций по дате"""
    sort_list = sorted(date, key=lambda x: x['date'], reverse=True)
    return sort_list  # список остортированных по дате операций


def executed_operations(operations: list) -> list:
    """сортирует список операций выполненные по ключу EXECUTED"""
    executed_list = []
    for execut in operations:
        if execut.get('state') is not None:
            if execut["state"] == 'EXECUTED':
                executed_list.append(execut)

    return executed_list  # список выполненных операций
