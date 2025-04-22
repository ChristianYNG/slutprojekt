class Account: # Klass för att skapa konton
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0.0
        self.history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount # Lägg till ett insättning
            print(f"{amount} SEK successfully deposited")
            self.history.append(f"deposit: {amount} SEK") # sparar insättningne i en lista
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


accounts = {} # En tom dict som håller alla kontonummer

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
            choice = input("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Transaction History\n5. Sign Out: ")

            if choice == "1" or choice.lower() == "check balance":
                user_account.check_balance()

            elif choice == "2" or choice.lower() == "deposit":
                amount = float(input("Enter amount to deposit: "))
                user_account.deposit(amount)

            elif choice == "3" or choice.lower() == "withdraw":
                amount = float(input("Enter amount to withdraw: "))
                user_account.withdraw(amount)

            elif choice == "4" or choice.lower() == "transaction history":
                print("Transaction History:")
                for entry in user_account.history:
                    print(entry)

            elif choice == "5" or choice.lower() == "sign out":
                print("Signed out successfully!")
                break  

            else:
                print("Invalid choice.")

    elif main_choice == "2":
        print("Thank you for banking with us!")
        break

    else:
        print("Invalid choice.")