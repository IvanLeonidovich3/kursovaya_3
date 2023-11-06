import json


#  14.10.2018
def load_operation():
    """загружает список операций"""
    with open('operations.json', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data  # список всех операций из json файла


def empty_operation():
    """проверка на пустой список"""
    len_list = []
    for k in load_operation():  # убераю пустой список
        if len(k) > 0:
            len_list.append(k)
    return len_list  # список всех не пустых операций


date = empty_operation()  # чистая перменная без пустых операций


def sort_date():
    """сортирует список операций по дате"""
    sort_list = sorted(date, key=lambda x: x['date'], reverse=True)
    return sort_list  # список остортированных по дате операций


def executed_operations():
    """сортирует список операций выполненные по ключу EXECUTED"""
    executed_list = []
    for execut in date:
        if execut["state"] == 'EXECUTED':
            executed_list.append(execut)
    return executed_list[:5]  # список выполненных операций


