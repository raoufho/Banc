import random
from Application.Core.Validator import Validator
from Application.Core.Account import Account
from Application.Core.VIPAccount import VIPAccount



class Bank:
    def __init__(self):
        # Initialize empty list to store accounts
        self._accounts = []

    def get_accounts(self):
        # Return list of accounts
        return self._accounts

    def get_account_by_number(self, number):
        # Retrieve account by account number
        for account in self._accounts:
            if account.get_account_number() == number:
                return account
        return None

    def _account_number_generator(self):
        # Generate a unique random account number
        while True:
            account_number = str(random.randint(100000, 999999))
            if self.get_account_by_number(account_number) is None:
                return account_number

    def create_account(self, is_vip=False):
        # Create a new account
        name = Validator.input_valid_name()                  # Get a valid name for the account
        password = Validator.input_valid_password()          # Get a valid password for the account
        account_number = self._account_number_generator()    # Generate a unique account number
        # Create either a VIP or normal account based on input
        account = VIPAccount(account_number, name, password) if is_vip else Account(account_number, name, password)
        self._accounts.append(account)          # Add account to list of accounts
        account_type = 'VIP ' if is_vip else ''
        print(f"{account_type}Account created with number: {account_number}")
        return True

    def log_in(self):
        # Log into an existing account
        number = Validator.input_valid_account_number()         # Get valid account number from user
        desire_account = self.get_account_by_number(number)     # Get account corresponding to the account numbe
        if desire_account is None:
            # If no account found, print error message
            print(f"No account found with number: {number}")
            return False
        password = Validator.input_valid_password()             # Get password from user
        if not desire_account.is_password(password):
            # If password is incorrect, print error message
            print("Incorrect password")
            return False
        if isinstance(desire_account, VIPAccount):
            # If logging into VIP account, print success message
            print(f"Connected successfully to VIP Account. Welcome {desire_account.get_name()}")
        else:
            # If logging into normal account, print success message
            print(f"Connected successfully. Welcome {desire_account.get_name()}")
        return desire_account
