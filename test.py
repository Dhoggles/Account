import pytest
from main import Account


def test_add_money():
    account = Account()
    account.add_money(100)
    assert account.get_balance() == 100


data = [
    ([10, 50, 100], 160),
    ([100, 3000, 1], 3101),
    ([210, 140, 100], 450),

]


# то что использует в def то и записываем в parametrize
@pytest.mark.parametrize("balance_list, expected_balance", data)
def test_add_money_1(balance_list, expected_balance):
    account = Account()
    for el in balance_list:
        account.add_money(el)
    assert account.get_balance() == expected_balance


data_1 = [
    (2000, [20, 50, 100], 1830),
    (1500, [30, 65, 1000], 405),
    (1700, [600, 1000, 100], 0),
]


@pytest.mark.parametrize("start_balance,balance, expected_balance", data_1)
def test_cross(start_balance, balance, expected_balance):
    account = Account()
    account.add_money(start_balance)
    for el in balance:
        account.withdraw_money(el)
    assert account.get_balance() == expected_balance


data_2 = [
    (1000, 1000),
    (100, 100),
    (15, 15)
]


@pytest.mark.parametrize("start_balance, expected_balance", data_2)
def test_balance(start_balance, expected_balance):
    account = Account()
    account.add_money(start_balance)
    assert account.get_balance() == expected_balance
