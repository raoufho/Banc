import sys
from Application.Core.Bank import Bank


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
