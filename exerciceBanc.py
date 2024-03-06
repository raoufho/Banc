import random
import string
import re
import getpass
import sys


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


class Validator:
    @staticmethod
    def is_valid_name(name: str) -> bool:
        # Validate name format
        name = name.strip()         # Remove leading and trailing whitespace
        # Check if the name contains at least three characters and follows the pattern of alphabetical characters with optional spaces
        # This pattern allows for names like "John", "John Doe", "John Michael Doe" ...etc
        return len(name) >= 3 and bool(re.fullmatch(r'^[A-Za-z]+(?: [A-Za-z]+)*$', name))

    @staticmethod
    def is_valid_password(password: str) -> bool:
        # Validate password format
        if len(password) < 8:
            return False
        has_uppercase = False
        for char in password:
            if char.isupper():
                has_uppercase = True
                break
        if not has_uppercase:
            return False
        has_lowercase = False
        for char in password:
            if char.islower():
                has_lowercase = True
                break
        if not has_lowercase:
            return False
        has_digit = False
        for char in password:
            if char.isdigit():
                has_digit = True
                break
        if not has_digit:
            return False
        has_symbol = False
        for char in password:
            if char in string.punctuation:
                has_symbol = True
                break
        if not has_symbol:
            return False
        return True

    @staticmethod
    def is_valid_amount(amount: str) -> bool:
        # Validate amount format
        try:
            amount = float(amount)
            if amount <= 0:
                print("Amount must be greater than zero.")
                return False
            return True
        except ValueError:
            print("Invalid amount. Please enter a valid numeric value.")
            return False

    @staticmethod
    def input_valid_account_number():
        # Validate account number format
        number = input("Enter your account number: ")
        while not (number.isdigit() and len(number) == 6):
            print(f"Invalid account number: {number}")
            number = input("Enter your account number again: ")
        return number

    @staticmethod
    def input_valid_name():
        # Get and validate user input for name
        name = input("Enter your name: ")
        while not Validator.is_valid_name(name):
            print(f"Invalid name {name}")
            name = input("Enter your name again: ")
        return name

    @staticmethod
    def input_valid_password():
        # Get and validate user input for password
        password = getpass.getpass("Enter your password: ")
        while not Validator.is_valid_password(password):
            print("Invalid password")
            password = getpass.getpass("Enter your password again: ")
        return password

    @staticmethod
    def valid_transfer(target_account_number):
        # Validate transfer details
        target_account = Application._bank.get_account_by_number(target_account_number)
        if target_account is None:
            print(f"No account found with number: {target_account_number}")
            return False

        amount = input("Enter the amount you want to transfer: ")
        if not Validator.is_valid_amount(amount):
            return False

        amount = float(amount)
        return amount, target_account


class Application:
    _bank = Bank()

    @staticmethod
    def start():
        # Start the banking application
        while True:
            print("\nWelcome to the Banking System!")
            options = {
                "1": "Create a new account",
                "2": "Access an existing account",
                "3": "Exit"
            }
            for key, value in options.items():
                print(f"{key}: {value}")

            choice = input("Enter the option number: ")

            if choice == "1":
                # Create a new account
                options = {
                    "1": {"type": "Normal", "is_vip": False},
                    "2": {"type": "VIP", "is_vip": True},
                }
                for key, value in options.items():
                    print(f"{key}: Create a '{value['type']}' account")

                option = input("Enter your choice: ")
                if option in options:
                    Application._bank.create_account(options[option]["is_vip"])
                    print(f"{options[option]['type']} account created successfully.")
                else:
                    print("Invalid option. Please enter 1 for 'Normal' or 2 for 'VIP'.")

            elif choice == "2":
                # Log into an existing account
                account = Application._bank.log_in()
                if account:
                    while True:
                        options = {
                            "1": "Withdraw",
                            "2": "Deposit",
                            "3": "Transfer amount",
                            "4": "Display balance",
                            "5": "Log-Out",
                            "6": "Exit"
                        }
                        for key, value in options.items():
                            print(f"{key}: {value}")

                        option = input("Enter the option number: ")

                        if option == "1":
                            amount = input("Enter the withdrawal amount: ")
                            account.withdraw(amount)

                        elif option == "2":
                            amount = input("Enter the deposit amount: ")
                            account.deposit(amount)

                        elif option == "3":
                            target_account_number = input("Enter the account number to which you want to make a transfer: ")
                            account.transfer(target_account_number)

                        elif option == "4":
                            account.display_balance()

                        elif option == "5":
                            print("Returning to the main menu")
                            break

                        elif option == "6":
                            print("Exiting the program. Thank you for using our service.\n")
                            sys.exit()

                        else:
                            print("Invalid option. Please enter a valid option (1-5).")

                else:
                    print("Invalid name or account number.")

            elif choice == "3":
                # Exit the program
                print("Exiting the program. Thank you for using our service.\n")
                break

            else:
                print("Invalid option. Please enter a valid option (1-3).")


if __name__ == '__main__':
    # Start the application
    Application.start()
