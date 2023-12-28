# self.accounts = {
#    "account_number_1": {"Name": "John Doe", "balance": 1000.0},
#    "account_number_2": {"Name": "Jane Smith", "balance": 500.0},
    # ... other accounts ...
# }


import random

class Bank:
    
    def __init__(self):
        self.accounts = {}


    def account_number_generator(self):
        while True:
            account_number = str(random.randint(1,99999)).zfill(5)
            if account_number not in self.accounts:
                return str(random.randint(1,99999)).zfill(5)


    def creataccount(self, name, initial_deposit):
        account_number = self.account_number_generator()
        self.accounts[account_number] = {'name': name, 'balance': initial_deposit}
        print("your account number is: ", account_number)
        

    def check_valid_user(self, name, account_number):
        if account_number in self.accounts and self.accounts[account_number]['name'] == name:
            return True
        else:
            return False

        
    def withdraw(self, account_number, amount):
        amount = float(amount)
        self.accounts[account_number]['balance'] -= amount
        print(f"Available balance: {self.accounts[account_number]['balance']}")
        

    def deposit(self, account_number, amount):
        amount = float(amount)
        self.accounts[account_number]['balance'] += amount
        print(f"Available balance: {self.accounts[account_number]['balance']}")

    def display(self, account_number):
        print("You have: ", self.accounts[account_number]['balance'])


bank = Bank()
while True:
    print("\nWelcome to the Banking System!")
    print("\n1 Creat a new account")
    print("2 Access to an existing account")
    print("3 Exit")
    
    choice = input("\nEnter the option number: ") 
    if choice == "1":
        name = input("Enter your name: ")
        initial_deposit = float(input("Enter your initial deposit amount: "))
        bank.creataccount(name, initial_deposit)

    elif choice == "2":
        name = input("Enter your name: ")
        account_number = input("Enter your account number: ")
        
        if bank.check_valid_user(name, account_number):

            while True:
                print("\nWhat would you like to do?")
                print("1: Withdraw: ")
                print("2: Deposit")
                print("3: Display balance")
                print("4: Return to the main menu")

                option = input("Enter the option number: ")     #int input doesn't work with string option

                if option == "1":
                    amount = input("Enter the withdrawal amount: ")
                    bank.withdraw(account_number, amount)

                elif option == "2":
                    amount = input("Enter the deposit amount: ")
                    bank.deposit(account_number, amount)

                elif option == "3":
                    bank.display(account_number)

                elif option == "4":
                    print("Reterning to the main menu")
                    break

                else:
                    print("Invalid option. Please enter a valid option (1, 2, 3, or 4).\n")
            
        else:
            print("Please check your name and account number\n")

    elif choice == "3":
        print("thank you for using our service\n")
        exit()

    else:
        print("Invalid option, Please enter a valid option (1, 2, or 3)")
