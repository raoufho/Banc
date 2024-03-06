import getpass
import re
import string


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
        # We utilize the import within the method to avoid  circular module issue
        from Application.Application import Application 
        target_account = Application._bank.account_with_number(target_account_number)
        if target_account is None:
            print(f"No account found with number: {target_account_number}")
            return False

        amount = input("Enter the amount you want to transfer: ")
        if not Validator.is_valid_amount(amount):
            return False

        amount = float(amount)
        return amount, target_account

