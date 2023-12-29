# Project:
# Let's create a project to simulate a banking system.
# You first need to provide a prompt to the user asking if they wish to create a new savings account or access an existing one.
# And if it is a new savings account that they wish to create, you need to accept their name and initial deposit And then in your program you need to have a five digit random number generator.
# And this random number will be the account number of their new savings account.
# And if it is an existing account that they wish to access you need to accept their name and account number and check if it's a valid user.
# And then you need to provide them options to withdraw, deposit or display their available balance if it is a valid user.

# Solution:
# self.accounts = {
#    "account_number_1": {"Name": "John Doe", "balance": 1000.0},
#    "account_number_2": {"Name": "Jane Smith", "balance": 500.0},
    # ... other accounts ...
# }
# {account_number : account_info} as account_info = {name : balance}


import random

class Bank:
    
    def __init__(self):
        # Initialize an empty dictionary to store account information
        # The dictionary contain the name and the account number as information
        self.accounts = {}

    def account_number_generator(self):
# we use while because we can randomly fall in the same account number and we need to re use the random
        while True:
            # Generate a random 5-digit account number with leading zeros
            account_number = str(random.randint(1,99999)).zfill(5)
            # Check if the account number is already in use
            if account_number not in self.accounts:
                return account_number

    def creataccount(self, name, initial_deposit):
        # Check if the user name lenght is more than three characters
        if len(name) > 3 :
            # Check if initial deposit is between 0 and 5000 
            if 10 <= initial_deposit < 5000 :
                # Check if a user with the same name already exists
                for account_number, account_info in self.accounts.items():
                    if account_info['name'] == name:
                        print(f"Error: Account creation failed. A user with the name '{name}' already exists.")
                        return
                # Create a new account with a random account number
                account_number = self.account_number_generator()
                # Store account information in the dictionary
                self.accounts[account_number] = {"name": name, "balance": initial_deposit}
                # Display a success message with the account number
                print(f"Account created successfully. Your account number is: {account_number}")
            else:
                print("Error: Initial deposit must be between 10 and 5000.")
        else:
            print("Error: User name must be more than 3 characters.")

    def check_valid_user(self, name, account_number):
    # Check if the provided account number and name match an existing account
        if account_number in self.accounts and self.accounts[account_number]['name'] == name:
            return True     # Return True if the account is valid
        else:
            return False    # Return False if the account is not valid

    def withdraw(self, account_number, amount):
        # Convert the withdrawal amount to a float
        amount = float(amount)
        # Check if there are sufficient funds for the withdrawal and amount is positive
        if amount > 0 and amount > self.accounts[account_number]['balance']:
            # Display an error message for insufficient funds
            print("Insufficient funds. Withdrawal failed.")
        else:
            # Perform the withdrawal and display the updated balance
            self.accounts[account_number]['balance'] -= amount
            print(f"Withdrawal successful. Available balance: {self.accounts[account_number]['balance']}")

    def deposit(self, account_number, amount):
        # Convert the deposit amount to a float
        amount = float(amount)
        # Check if the amount is positif and less than 10k
        if 0 < amount < 10000 :
            # Perform the deposit and display the updated balance
            self.accounts[account_number]['balance'] += amount
            print(f"Deposit successful. Available balance: {self.accounts[account_number]['balance']}")
        else:
            # Message error for deposit
            print("Deposit failed. Amount should be less than 10000")

    def display(self, account_number):
        # Display the available balance for the specified account
        print("Available balance: ", self.accounts[account_number]['balance'])

# Initialize the bank object
bank = Bank()

# Main loop for the banking system
while True:
    print("\nWelcome to the Banking System!")
    print("1- Creat a new account")
    print("2- Access to an existing account")
    print("3- Exit")
    
    # Get user input for the main menu options
    choice = input("Enter the option number: ") 
    
    if choice == "1":
        # Option to create a new account
        name = input("Enter your name: ")
        initial_deposit = float(input("Enter your initial deposit amount: "))
        bank.creataccount(name, initial_deposit)

    elif choice == "2":
        # Option to access an existing account
        name = input("Enter your name: ")
        account_number = input("Enter your account number: ")
        
        if bank.check_valid_user(name, account_number):
        # Access granted, show additional options for the account
            while True:
                print("\nWhat would you like to do?")
                print("1: Withdraw ")
                print("2: Deposit")
                print("3: Display balance")
                print("4: Return to the main menu")
                print("5: Exit")

                # Get user input for the account options
                option = input("Enter the option number: ")  #int input doesn't work with string options "1"

                if option == "1":
                    # Option to withdraw funds
                    amount = input("Enter the withdrawal amount: ")
                    bank.withdraw(account_number, amount)

                elif option == "2":
                    # Option to deposit funds
                    amount = input("Enter the deposit amount: ")
                    bank.deposit(account_number, amount)

                elif option == "3":
                    # Option to display available balance
                    bank.display(account_number)

                elif option == "4":
                    # Option to return to the main menu
                    print("Reterning to the main menu")
                    break

                elif option == "5":
                    # Option to exit the program
                    print("Exiting the program. Thank you for using our service\n")
                    exit()

                else:
                    # Display an error message for invalid options
                    print("Invalid option. Please enter a valid option (1, 2, 3, or 4).\n")
            
        else:
            # Display an error message for invalid user or account
            print("Invalid option. Please check your name and account number\n")

    elif choice == "3":
        # Option to exit the program
        print("Exiting the program. Thank you for using our service\n")
        exit()

    else:
        # Display an error message for invalid main menu options
        print("Invalid option, Please enter a valid option (1, 2, or 3)")
