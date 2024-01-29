import random

class Account:

    def __init__(self, name, initial_deposit):
        self.name = name
        self.balance = initial_deposit

class Bank:
    
    def __init__(self):
        # Initialize an empty dictionary to store account information
        # The dictionary contain the account number, the name and the balance as information
        self._accounts = {}

    def _account_number_generator(self):
    # we use while because we can randomly fall in the same account number and we need to reuse the random
        while True:
            # Generate a random 5-digit account number with leading zeros
            account_number = str(random.randint(1,99999)).zfill(5)
            # Check if the account number is already in use
            if account_number not in self._accounts:
                return account_number

    def creat_account(self, name, initial_deposit):
        # Check if the user name lenght is more than three characters and initial deposit is between 0 and 5000 
        if len(name) > 3 and 10 <= initial_deposit < 5000:
            # Check if a user with the same name already exists
            for account_number, account_info in self._accounts.items():
                if account_info.name == name:
                # each account is represented as an instance of the Account class
                    print(f"Error: Account creation failed. A user with the name '{name}' already exists.")
                    return
            # Create a new account with a random account number
            account_number = self._account_number_generator()
            new_account = Account(name, initial_deposit)
            # Store account information in the dictionary
            self._accounts[account_number] = new_account
            # Display a success message with the account number
            print(f"Account created successfully. Your account number is: {account_number}")
        else:
            print("Error: Invalid user name or initial deposit amount.")
    

    def _check_valid_user(self, name, account_number):
    # Check if the provided account number and name match an existing account
        if account_number in self._accounts and self._accounts[account_number].name == name:
            return True     # Return True if the account is valid
        else:
            return False    # Return False if the account is not valid

    def withdraw(self, account_number, amount):
        try:
            # Convert the withdrawal amount to a float
            amount = float(amount)
            # Check if there are sufficient funds for the withdrawal and amount is positive
            if 0 < amount < self._accounts[account_number].balance:
                # Perform the withdrawal and display the updated balance
                self._accounts[account_number].balance -= amount
                print(f"Withdrawal successful. Available balance: ${self._accounts[account_number].balance:.2f}")
            else:
                # Display an error message for insufficient funds
                print("Insufficient funds. Withdrawal failed.")

        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")
        return

    def deposit(self, account_number, amount):
        try:
            # Convert the deposit amount to a float
            amount = float(amount)
            # Check if the amount is positif and less than 10k
            if 0 < amount < 10000 :
                # Perform the deposit and display the updated balance
                self._accounts[account_number].balance += amount
                print(f"Deposit successful. Available balance: ${self._accounts[account_number].balance :.2f}")
            else:
                # Message error for deposit
                print("Deposit failed. Amount should be less than $10000")
                
        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")
        return
    
    def transfer(self, account_number, account_transfer):
        try:
            # Check if the provided account number for transfer exists   
            if account_transfer in self._accounts:
                # Get the transfer amount from user input
                amount = input("Enter the amount: ")
                amount = float(amount)
                # Check if the amount is positive and within the available balance
                if 0 < amount <= self._accounts[account_number].balance:
                    # Perform the transfer by deducting from the sender and adding to the receiver
                    self._accounts[account_number].balance -= amount
                    self._accounts[account_transfer].balance += amount
                    print("Transfer successful.")
                else:
                    # Display an error message for invalid account number for transfer
                    print("Insufficient funds. Transfer failed.")
            else:
                print("This account number doesn't exist")
        
        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")
        return

    def display(self, account_number):
        # Display the available balance for the specified account
        print("Available balance: ${:.2f}".format(self._accounts[account_number].balance))

class Menu:

    def __init__(self):
        self._bank = Bank()

    @staticmethod
    def start():
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
                self._bank.creat_account(name, initial_deposit)

            elif choice == "2":
                # Option to access an existing account
                name = input("Enter your name: ")
                account_number = input("Enter your account number: ")
                
                if self._bank._check_valid_user(name, account_number):

                # Access granted, show additional options for the account
                    while True:
                        print("\nWhat would you like to do?")
                        print("1: Withdraw ")
                        print("2: Deposit")
                        print("3: Transfer amount")
                        print("4: Display balance")
                        print("5: Return to the main menu")
                        print("6: Exit")

                        # Get user input for the account options
                        option = input("Enter the option number: ")  #int input doesn't work with string options "1"

                        if option == "1":
                            # Option to withdraw funds
                            amount = input("Enter the withdrawal amount: ")
                            self._bank.withdraw(account_number, amount)

                        elif option == "2":
                            # Option to deposit funds
                            amount = input("Enter the deposit amount: ")
                            self._bank.deposit(account_number, amount)

                        elif option == "3":
                            # Option to transfer amount
                            account_transfert = input("Enter the account number to which you want to make a transfer: ")
                            self._bank.transfer(account_number, account_transfert)    

                        elif option == "4":
                            # Option to display available balance
                            self._bank.display(account_number)

                        elif option == "5":
                            # Option to return to the main menu
                            print("Reterning to the main menu")
                            break

                        elif option == "6":
                            # Option to exit the program
                            print("Exiting the program. Thank you for using our service\n")
                            exit()

                        else:
                            # Display an error message for invalid options
                            print("Invalid option. Please enter a valid option\n")
                    
                else:
                    # Display an error message for invalid user or account
                    print("Invalid option. Please check your name and account number\n")

            elif choice == "3":
                # Option to exit the program
                print("Exiting the program. Thank you for using our service\n")
                break   # Exit the main loop

            else:
                # Display an error message for invalid main menu options
                print("Invalid option, Please enter a valid option (1, 2, or 3)")

# Initialize and start the banking system
menu = Menu()
menu.start()

""" 
Project:
 Let's create a project to simulate a banking system.
 first you need to provide a prompt to the user asking if they wish to create a new savings account or access an existing one.
 if it is a new savings account that they wish to create, you need to accept their name and initial deposit And then in your program you need to have a five digit random number generator.
 And this random number will be the account number of their new savings account.
 if it is an existing account that they wish to access you need to accept their name and account number and check if it's a valid user.
 And then you need to provide them options to withdraw, deposit or display their available balance if it is a valid user.

 Solution:
 self._accounts = {
    'account_number_1': Account('account_name_1', account_balance_1),
    'account_number_2': Account('account_name_2', account_balance_2),
    # ... and so on
}

 """