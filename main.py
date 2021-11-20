class Account:

    def __init__(self):
        self.balance = 0

    def add_money(self, number):
        assert number >= 0
        self.balance += int(number)

    def get_balance(self):
        return self.balance

    def withdraw_money(self, number):
        if number <= self.balance:
            self.balance -= number
            return True
        return False
