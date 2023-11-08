from src.utils import load_operation, executed_operations, sort_date
from src.masks import transform_date, mask_count_card, account_mask

operations = load_operation()  # загрузил список
sorted_operations = executed_operations(operations)  # отсорировал операции по EXECUTED
sorted_date = sort_date(sorted_operations)[:5]  # отсортировал по убываню даты последние 5
card_name = mask_count_card(sorted_date)  # замаскировал номер карты
account_number = account_mask(sorted_date)
for operation in sorted_date:
    print(f'{transform_date(operation["date"])} {operation.get("description")}')
    print(f'{mask_count_card(operation.get("from", "--"))} -> {"Счет"} {account_mask(operation.get("to"))}')
    print(f'{operation.get("operationAmount")["amount"]} {operation.get("operationAmount")["currency"]["name"]}')
    print()
