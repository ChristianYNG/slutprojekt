from tkinter import *
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk

# Skapa huvudfönster
window = Tk()
window.title("SEB Bank: Log In")
window.geometry('800x800')
window.configure(bg='lightgreen')

# === LOGO FRAME ===
logo_frame = Frame(window, bg='lightgreen')
logo_frame.pack(side='top', padx=0)

Seblogo = Image.open(r"C:\Users\christian.young\Desktop\Filhantering\Slutprojekt\seblogopng.png")
Seblogo = Seblogo.resize((300, 150))
photo = ImageTk.PhotoImage(Seblogo)

label_logo = Label(logo_frame, image=photo, bg='lightgreen')
label_logo.image = photo
label_logo.pack()

# === CONTENT FRAME ===
content_frame = Frame(window, bg='lightgreen')
content_frame.pack(expand=True, fill='both')

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
    clear_window()

    frame = Frame(content_frame, bg='lightgreen')
    frame.place(relx=0.5, rely=0.5, anchor='center')

    Label(frame, text=f"Account {user_account.account_number} - Menu", bg="green").pack(pady=10)
    Button(frame, text="Check Balance", width=20, command=user_account.check_balance).pack(pady=5)
    Button(frame, text="Deposit", width=20, command=gui_deposit).pack(pady=5)
    Button(frame, text="Withdraw", width=20, command=gui_withdraw).pack(pady=5)
    Button(frame, text="Transfer", width=20, command=gui_transfer).pack(pady=5)
    Button(frame, text="Transaction History", width=20, command=show_history).pack(pady=5)
    Button(frame, text="Sign Out", width=20, command=restart).pack(pady=5)

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
    clear_window()
    draw_login()

def exit_app():
    messagebox.showinfo("Exit", "Thank you for banking with us!")
    window.destroy()

def clear_window():
    for widget in content_frame.winfo_children():
        widget.destroy()

# Första inloggningsformuläret
def draw_login():
    clear_window()

    frame = Frame(content_frame, bg='lightgreen')
    frame.place(relx=0.5, rely=0.5, anchor='center')

    Label(frame, text="Account Number:", bg="white").pack(pady=10)
    global account_entry
    account_entry = Entry(frame)
    account_entry.pack()

    Button(frame, text="Sign In", width=20, command=sign_in).pack(pady=5)
    Button(frame, text="Exit", width=20, command=exit_app).pack(pady=5)

# Starta GUI
draw_login()
window.mainloop()
