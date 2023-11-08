def transform_date(date: str) -> str:
    """преобразовывает дату в необходимый формат ДД.ММ.ГГГГ"""
    dat_n = date.split('T')[0].split('-')
    return f'{dat_n[2]}.{dat_n[1]}.{dat_n[0]}'


def mask_count_card(card_name: str) -> str:
    """принимает на вход строку информацией тип карты/счета и номер карты/счета
    card_name - имя карты, её номер и счет
    возвращает строку с замаскированным номером карты/счета"""
    str_number = str(card_name).split()[-1]
    stars_number = str_number[:6] + (len(str_number[6:-4]) * "*") + str_number[-4:]
    mask_number = stars_number[0:4] + " " + stars_number[4:8] + " " + stars_number[8:12] + " " + stars_number[-4:]
    return mask_number


def account_mask(account_number: int) -> str:
    """получает и маскируетмаску счета"""
    get_account = account_number
    str_account = str(get_account)
    mask_account = "*" * len(str_account[:2]) + str_account[-4:]
    return mask_account
