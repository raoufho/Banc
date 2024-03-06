from Application.Core.Account import Account
from Application.Core.Validator import Validator


class VIPAccount(Account):
    def __init__(self, account_number, name, password):
        # Initialize VIP account
        super().__init__(account_number, name, password)
        self._is_vip = True
        self._balance = 1000

    def withdraw(self, amount):
        # Withdraw funds from VIP account
        if self._is_vip:
            if not Validator.is_valid_amount(amount):
                return False
            amount = float(amount)
            if amount > self.get_balance():
                print("Insufficient funds. Withdrawal failed.")
                return False
            self.set_balance(self.get_balance() - amount)
            print("Withdraw successful:", amount)
            return True
        else:
            print("VIP account cannot withdraw.")
            return False

    def deposit(self, amount):
        # Deposit funds into VIP account
        if not Validator.is_valid_amount(amount):
            return False
        amount = float(amount)
        self.set_balance(self.get_balance() + amount)
        print("Deposit successful:", amount)
        return True

        target_account = Application._bank.get_account_by_number(target_account_number)
        if target_account is None:
            print(f"No account found with number: {target_account_number}")
            return False
        amount = input("Enter the amount you want to transfer: ")
        if not Validator.is_valid_amount(amount):
            return False
        amount = float(amount)
        if amount > self.get_balance():
            print("Insufficient funds. Transfer failed.")
            return False
        self.set_balance(self.get_balance() - amount)
        target_account.set_balance(target_account.get_balance() + amount)
        return True

    def transfer(self, target_account_number):
        # Transfer funds from VIP account to another account
        transfer_data = Validator.valid_transfer(target_account_number)
        if not transfer_data:
            return False

        amount, target_account = transfer_data
        if amount > self.get_balance():
            print("Insufficient funds. Transfer failed.")
            return False

        self.set_balance(self.get_balance() - amount)
        target_account.set_balance(target_account.get_balance() + amount)
        return True
