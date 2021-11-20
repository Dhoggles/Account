import pytest
from main import Account


def test_add_money():
    account = Account()
    account.add_money(100)
    assert account.get_balance() == 100


data = [
    ([100, 1000, 100], 1200),
    ([100, 1000, 100], 1200),
    ([100, 1000, 100], 1200),

]


# то что использует в def то и записываем в parametrize
@pytest.mark.parametrize("balance_list, expected_balance", data)
def test_add_money_1(balance_list, expected_balance):
    account = Account()
    for el in balance_list:
        account.add_money(el)
    assert account.get_balance() == expected_balance


data_1 = [
    (2000, [20, 50, 100], 1830)
]


@pytest.mark.parametrize("start_balance,balance, expected_balance", data_1)
def test_cross(start_balance, balance, expected_balance):
    account = Account()
    account.add_money(start_balance)
    for el in balance:
        account.withdraw_money(el)
    assert account.get_balance() == expected_balance
