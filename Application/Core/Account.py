from Application.Core.Validator import Validator


class Account:
    def __init__(self, account_number, name, password):
        # Initialize account attributes
        self.__withdraw_fee = 30
        self._max_deposit_amount = 200000
        self._balance = 0
        self._account_number = account_number
        self._password = password
        self._name = name
        self._deposit_fee = 0.05 / 100
        self._transfer_fee = 0.05 / 100
        
    def get_name(self):
        # Get account holder's name
        return self._name.capitalize()

    def get_balance(self):
        # Get current account balance
        return self._balance

    def get_account_number(self):
        # Get account number
        return self._account_number

    def set_balance(self, balance):
        # Set account balance
        self._balance = balance

    def set_password(self, password):
        # Set account password, we didn't used it yet
        self._password = password

    def is_password(self, password):
        # Check if provided password matches account password
        return password == self._password

    def withdraw(self, amount):
        # Withdraw funds from account
        if not Validator.is_valid_amount(amount):
            return False
        amount = float(amount)
        total_withdraw = amount + self.__withdraw_fee
        if total_withdraw > self.get_balance():
            print("Insufficient funds. Withdrawal failed.")
            return False
        self.set_balance(self.get_balance() - total_withdraw)
        print("Withdraw successful:", amount)
        return True

    def deposit(self, amount):
        # Deposit funds into account
        if not Validator.is_valid_amount(amount):
            return False
        amount = float(amount)
        if amount > self._max_deposit_amount:
            print(f"Deposit failed. Amount should be less than ${self._max_deposit_amount}")
            return False
        total_deposit = amount - (amount * self._deposit_fee)
        self.set_balance(self.get_balance() + total_deposit)
        print("Deposit successful:", amount)
        return True

    def transfer(self, target_account_number):
        # Transfer funds to another account
        transfer_data = Validator.valid_transfer(target_account_number)
        if not transfer_data:
            return False

        amount, target_account = transfer_data
        total_transfer = amount + (amount * self._transfer_fee)
        if total_transfer > self.get_balance():
            print("Insufficient funds. Transfer failed.")
            return False

        self.set_balance(self.get_balance() - total_transfer)
        target_account.set_balance(target_account.get_balance() + amount)
        return True

    def display_balance(self):
        # Display account balance
        print(f"Current balance: {self.get_balance()}")


