import random

class Bank:
    
    def __init__(self):
        accounts = {}

    def creataccount(self, name, initial_deposit):
        print("Enter your name: ")
        name = input(name)
        print("Enter your initial deposit: ")
        initial_deposit = input(int(initial_deposit))

    def account_number_generator(self):
        self.account_number = random.randint(1,99999).zfill(5)

    def check_valid_user(self, name, account_number):
        #for name, account_numbers in account.items() :
            #for account_number in account_numbers:
        pass

        
    def withdraw(self, initial_deposit):
        amount = input()
        initial_deposit -= amount
        print("You have :",initial_deposit)

    def deposit(self, initial_deposit):
        amount = input()
        initial_deposit += amount
        print('You have :',initial_deposit)

    def display(self, initial_deposit):
        print("You have: ", initial_deposit)


bank = Bank()
while True:
    print("Welcome!")
    print("Press 1 to creat a new account")
    print("Press 2 to access to an existing account")
    print("Press 3 to exit")
    
    choice = input() 
    if choice == "1":
        bank.creataccount()
        print("your account number is: ", bank.account_number_generator())

    elif choice == "2":
        print("Enter you name: ", input(""))
        print("Enter your deposit amount: ", input())
        bank.check_valid_user()

        while True:
            print("1: Withdraw: ")
            print("2: Deposit")
            print("3: Display balance")
            print("4: Return to the main menu")

            option = input(int())

            if option == 1:
                bank.withdraw()

            elif option == 2:
                bank.deposit()

            elif option == 3:
                bank.deposit()

            elif option == 4:
                break

            else:
                print("Invalid option. Please enter a valid option (1, 2, 3, or 4).")


    elif choice == "3":
        print("thank you for using our service")
        exit()

    else:
        print("Invalid option")
