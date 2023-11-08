from src.masks import mask_count_card, account_mask, transform_date


def test_mask_count_card():
    assert mask_count_card("Visa Classic 6831982476737658") == "6831 98** **** 7658"
    assert mask_count_card("Maestro 3928549031574026") == "3928 54** **** 4026"
    assert mask_count_card("none") == "none none  none"


def test_account_mask():
    assert account_mask("Счет 72082042523231456215") == "**6215"
    assert account_mask("none") == "**none"
    assert account_mask("999") == "**999"


def test_transform_date():
    assert transform_date("2019-12-08T22:46:21.935582") == "08.12.2019"

