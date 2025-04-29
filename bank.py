from tkinter import *
from tkinter import simpledialog, messagebox

# Skapa huvudfönster
window = Tk()
window.title("SEB Bank: Log In")
window.geometry('400x400')
window.configure(bg='lightgreen') 


accounts = {}
user_account = None  # Global variabel för inloggat konto

class Account:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0.0
        self.history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.history.append(f"Deposit: {amount} SEK")
        else:
            messagebox.showerror("Error", "Deposit must be more than 0")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.history.append(f"Withdraw: -{amount} SEK")
        else:
            messagebox.showerror("Error", "Insufficient funds or invalid amount")

    def check_balance(self):
        messagebox.showinfo("Balance", f"Balance: {self.balance} SEK")

    def transfer(self, amount, target_account_number):
        if 0 < amount <= self.balance:
            if target_account_number not in accounts:
                accounts[target_account_number] = Account(target_account_number)
                accounts[target_account_number].history.append(f"Created by transfer from {self.account_number}")
            target_account = accounts[target_account_number]
            self.balance -= amount
            target_account.balance += amount
            self.history.append(f"Transfer: -{amount} SEK to {target_account_number}")
            target_account.history.append(f"Transfer: +{amount} SEK from {self.account_number}")
            messagebox.showinfo("Success", f"Transferred {amount} SEK to {target_account_number}")
        else:
            messagebox.showerror("Error", "Insufficient funds or invalid amount")

# Logik för GUI
def sign_in():
    global user_account
    try:
        account_number = int(account_entry.get())
        if account_number in accounts:
            user_account = accounts[account_number]
            messagebox.showinfo("Logged In", f"Welcome back, account {account_number}!")
        else:
            user_account = Account(account_number)
            accounts[account_number] = user_account
            messagebox.showinfo("New Account", f"New account {account_number} created.")
        show_main_menu()
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid account number.")

def show_main_menu():
    for widget in window.winfo_children():
        widget.destroy()

    Label(window, text=f"Account {user_account.account_number} - Menu", bg="green").pack(pady=10)
    Button(window, text="Check Balance", command=user_account.check_balance).pack(pady=5)
    Button(window, text="Deposit", command=gui_deposit).pack(pady=5)
    Button(window, text="Withdraw", command=gui_withdraw).pack(pady=5)
    Button(window, text="Transfer", command=gui_transfer).pack(pady=5)
    Button(window, text="Transaction History", command=show_history).pack(pady=5)
    Button(window, text="Sign Out", command=restart).pack(pady=5)

def gui_deposit():
    amount = simpledialog.askfloat("Deposit", "Enter amount to deposit:")
    if amount is not None:
        user_account.deposit(amount)

def gui_withdraw():
    amount = simpledialog.askfloat("Withdraw", "Enter amount to withdraw:")
    if amount is not None:
        user_account.withdraw(amount)

def gui_transfer():
    amount = simpledialog.askfloat("Transfer", "Enter amount to transfer:")
    target = simpledialog.askinteger("Transfer", "Enter target account number:")
    if amount is not None and target is not None:
        user_account.transfer(amount, target)

def show_history():
    if user_account.history:
        messagebox.showinfo("History", "\n".join(user_account.history))
    else:
        messagebox.showinfo("History", "No transactions yet.")

def restart():
    for widget in window.winfo_children():
        widget.destroy()
    draw_login()

def exit_app():
    messagebox.showinfo("Exit", "Thank you for banking with us!")
    window.destroy()

# Första inloggningsformuläret
def draw_login():
    Label(window, text="Account Number:", bg="white").pack(pady=10)
    global account_entry
    account_entry = Entry(window)
    account_entry.pack()

    Button(window, text="Sign In", command=sign_in).pack(pady=5)
    Button(window, text="Exit", command=exit_app).pack(pady=5)

# Starta GUI
draw_login()
window.mainloop()
