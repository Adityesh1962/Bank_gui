import tkinter as tk
from tkinter import messagebox

class BankAccount:
    account_counter = 1000

    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance
        self.account_number = BankAccount.account_counter
        BankAccount.account_counter += 1

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return self.balance

    def get_balance(self):
        return self.balance

    def get_account_number(self):
        return self.account_number

class BankingSystem(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Banking System")
        self.geometry("1000x950")
        self.configure(bg="#2c3e50")

        self.accounts = {}

        self.create_widgets()

    def create_widgets(self):
        self.label_title = tk.Label(self, text="Welcome to python Bank", bg="#2c3e50", fg="#ecf0f1", font=("Helvetica", 16, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=3, pady=20)

        self.label_name = tk.Label(self, text="Name:", bg="#2c3e50", fg="#ecf0f1", font=("Helvetica", 12))
        self.label_name.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        self.entry_name = tk.Entry(self, font=("Helvetica", 12))
        self.entry_name.grid(row=1, column=1, padx=10, pady=10, sticky=tk.EW)

        self.button_create = tk.Button(self, text="Create Account", command=self.create_account, bg="#2980b9", fg="white", font=("Helvetica", 12))
        self.button_create.grid(row=1, column=2, padx=10, pady=10)

        self.label_account = tk.Label(self, text="Account No:", bg="#2c3e50", fg="#ecf0f1", font=("Helvetica", 12))
        self.label_account.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

        self.entry_account = tk.Entry(self, font=("Helvetica", 12))
        self.entry_account.grid(row=2, column=1, padx=10, pady=10, sticky=tk.EW)

        self.label_amount = tk.Label(self, text="Amount:", bg="#2c3e50", fg="#ecf0f1", font=("Helvetica", 12))
        self.label_amount.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)

        self.entry_amount = tk.Entry(self, font=("Helvetica", 12))
        self.entry_amount.grid(row=3, column=1, padx=10, pady=10, sticky=tk.EW)

        self.button_deposit = tk.Button(self, text="Deposit", command=self.deposit, bg="#2980b9", fg="white", font=("Helvetica", 12))
        self.button_deposit.grid(row=4, column=0, columnspan=3, pady=10, sticky=tk.EW)

        self.button_withdraw = tk.Button(self, text="Withdraw", command=self.withdraw, bg="#2980b9", fg="white", font=("Helvetica", 12))
        self.button_withdraw.grid(row=5, column=0, columnspan=3, pady=10, sticky=tk.EW)

        self.button_balance = tk.Button(self, text="Check Balance", command=self.check_balance, bg="#2980b9", fg="white", font=("Helvetica", 12))
        self.button_balance.grid(row=6, column=0, columnspan=3, pady=10, sticky=tk.EW)

    def create_account(self):
        name = self.entry_name.get()
        if name:
            account = BankAccount(name)
            self.accounts[account.get_account_number()] = account
            messagebox.showinfo("Info", f"Account created for {name}\nAccount Number: {account.get_account_number()}")
        else:
            messagebox.showwarning("Warning", "Please enter a name")

    def deposit(self):
        account_number = self.get_account_number()
        if account_number is not None:
            account = self.accounts.get(account_number)
            if account:
                amount = self.get_amount()
                if amount is not None:
                    account.deposit(amount)
                    messagebox.showinfo("Info", f"Deposit successful\nNew Balance: {account.get_balance()}")
            else:
                messagebox.showwarning("Warning", "Account number not found")

    def withdraw(self):
        account_number = self.get_account_number()
        if account_number is not None:
            account = self.accounts.get(account_number)
            if account:
                amount = self.get_amount()
                if amount is not None:
                    result = account.withdraw(amount)
                    if result == "Insufficient funds":
                        messagebox.showwarning("Warning", "Insufficient funds")
                    else:
                        messagebox.showinfo("Info", f"Withdrawal successful\nNew Balance: {account.get_balance()}")
            else:
                messagebox.showwarning("Warning", "Account number not found")

    def check_balance(self):
        account_number = self.get_account_number()
        if account_number is not None:
            account = self.accounts.get(account_number)
            if account:
                balance = account.get_balance()
                messagebox.showinfo("Info", f"Account Number: {account_number}\nCurrent Balance: {balance}")
            else:
                messagebox.showwarning("Warning", "Account number not found")

    def get_account_number(self):
        try:
            account_number = int(self.entry_account.get())
            return account_number
        except ValueError:
            messagebox.showwarning("Warning", "Please enter a valid account number")
            return None

    def get_amount(self):
        try:
            amount = float(self.entry_amount.get())
            return amount
        except ValueError:
            messagebox.showwarning("Warning", "Please enter a valid amount")
            return None

if __name__ == "__main__":
    app = BankingSystem()
    app.mainloop()

