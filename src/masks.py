def transform_date(date: str) -> str:
    """преобразовывает дату в необходимый формат ДД.ММ.ГГГГ"""
    dat_n = date.split('T')[0].split('-')
    return f'{dat_n[2]}.{dat_n[1]}.{dat_n[0]}'


