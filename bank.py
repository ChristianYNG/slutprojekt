class Account: # Klass för att skapa konton
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0.0
        self.history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount # Lägg till ett insättning
            print(f"{amount} SEK successfully deposited to account {self.account_number} ")
            self.history.append(f"deposit: {amount} SEK") # sparar insättningen i en lista
        else:
            print("Deposit must be larger than 0 SEK")
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.history.append(f"Uttag: -{amount} SEK")
        else: 
            print("Error withdrawing given amount")

    def check_balance(self):
        print(f"Available Balance: {self.balance} SEK")

    def transfer(self, transfer_amount, target_account_number):
        if 0 < transfer_amount <= self.balance:
            if target_account_number in accounts:
                target_account = accounts[target_account_number]
            else:
                print(f"Account {target_account_number} does not exist. Creating a new account.")
                target_account = Account(target_account_number)
                accounts[target_account_number] = target_account

            self.balance -= transfer_amount
            target_account.balance += transfer_amount
            self.history.append(f"Transfer: -{transfer_amount} SEK to account {target_account_number}")
            target_account.history.append(f"Transfer: +{transfer_amount} SEK from account {self.account_number}")
            print(f"{transfer_amount} SEK successfully transferred to account {target_account_number}")
        else:
            print("Error transferring given amount")


accounts = {} 
while True:
    print("\n1. Sign In\n2. Exit")
    main_choice = input("Choose an option: ")

    if main_choice == "1" or main_choice.lower == "sign in":
        account_number = int(input("Account Number: ")) 

        if account_number in accounts: # Kollar om kontot redan finns
            user_account = accounts[account_number]
        else: # Adderar kontonummer till tomma dicten om den inte finns
            print("New account created")
            user_account = Account(account_number)
            accounts[account_number] = user_account

        # Meny loop
        while True:
            choice = input("\n1. Check Balance\n2. Deposit\n3. Withdraw  \n4. Transfer \n5. Transaction History\n 6. Log out: ")

            if choice == "1" or choice.lower() == "check balance":
                user_account.check_balance()

            elif choice == "2" or choice.lower() == "deposit":
                amount = float(input("Enter amount to deposit: "))
                user_account.deposit(amount)

            elif choice == "3" or choice.lower() == "withdraw":
                amount = float(input("Enter amount to withdraw: "))
                user_account.withdraw(amount)

            elif choice == "4" or choice.lower() == "transfer":
                transfer_amount = float(input("Enter amount to transfer: "))
                target_account_number = int(input("Enter target account number: "))
                user_account.transfer(transfer_amount, target_account_number)

            elif choice == "5" or choice.lower() == "transaction history":
                print("Transaction History:")
                for entry in user_account.history:
                    print(entry)

            elif choice == "6" or choice.lower() == "sign out":
                print("Signed out successfully!")
                break  

            else:
                print("Invalid choice.")

    elif main_choice == "2":
        print("Thank you for banking with us!")
        break

    else:
        print("Invalid choice.")