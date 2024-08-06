import tkinter as tk
from tkinter import messagebox

class BankAccount:
    account_counter = 1000

    def __init__(self, owner, phone, address, balance=0.0):
        self.owner = owner
        self.phone = phone
        self.address = address
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

    def get_details(self):
        return f"Name: {self.owner}\nAccount Number: {self.account_number}\nPhone No: {self.phone}\nAddress: {self.address}\nBalance: {self.balance}"

class BankingSystem(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Banking System")
        self.attributes('-fullscreen', True)
        self.configure(bg="#2c3e50")

        self.accounts = {}

        self.create_initial_window()

    def create_initial_window(self):
        self.clear_window()

        self.label_title = tk.Label(self, text="Welcome to Python Bank", bg="#2c3e50", fg="#ecf0f1", font=("Helvetica", 24, "bold"))
        self.label_title.pack(pady=20, anchor="center")

        self.button_create_account = tk.Button(self, text="Create Account", command=self.create_account_window, bg="#2980b9", fg="white", font=("Helvetica", 16))
        self.button_create_account.pack(pady=20, anchor="center")

        self.button_login_account = tk.Button(self, text="Log in to your Account", command=self.login_account_window, bg="#2980b9", fg="white", font=("Helvetica", 16))
        self.button_login_account.pack(pady=20, anchor="center")

    def create_account_window(self):
        self.clear_window()

        self.label_name = tk.Label(self, text="Name:", bg="#2c3e50", fg="#ecf0f1", font=("Helvetica", 16))
        self.label_name.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)

        self.entry_name = tk.Entry(self, font=("Helvetica", 16))
        self.entry_name.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        self.label_phone = tk.Label(self, text="Phone No:", bg="#2c3e50", fg="#ecf0f1", font=("Helvetica", 16))
        self.label_phone.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)

        self.entry_phone = tk.Entry(self, font=("Helvetica", 16))
        self.entry_phone.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        self.label_address = tk.Label(self, text="Address:", bg="#2c3e50", fg="#ecf0f1", font=("Helvetica", 16))
        self.label_address.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)

        self.entry_address = tk.Entry(self, font=("Helvetica", 16))
        self.entry_address.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

        self.label_amount = tk.Label(self, text="Initial Deposit:", bg="#2c3e50", fg="#ecf0f1", font=("Helvetica", 16))
        self.label_amount.grid(row=3, column=0, padx=10, pady=10, sticky=tk.E)

        self.entry_amount = tk.Entry(self, font=("Helvetica", 16))
        self.entry_amount.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)

        self.button_create = tk.Button(self, text="Create Account", command=self.create_account, bg="#2980b9", fg="white", font=("Helvetica", 16))
        self.button_create.grid(row=4, column=0, padx=10, pady=10, columnspan=2)

        self.button_back = tk.Button(self, text="Back", command=self.create_initial_window, bg="#e74c3c", fg="white", font=("Helvetica", 16))
        self.button_back.grid(row=5, column=0, padx=10, pady=10, columnspan=2)

    def login_account_window(self):
        self.clear_window()

        self.label_account = tk.Label(self, text="Account No:", bg="#2c3e50", fg="#ecf0f1", font=("Helvetica", 16))
        self.label_account.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)

        self.entry_account = tk.Entry(self, font=("Helvetica", 16))
        self.entry_account.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        self.label_phone = tk.Label(self, text="Phone No:", bg="#2c3e50", fg="#ecf0f1", font=("Helvetica", 16))
        self.label_phone.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)

        self.entry_phone = tk.Entry(self, font=("Helvetica", 16))
        self.entry_phone.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        self.label_name = tk.Label(self, text="Name:", bg="#2c3e50", fg="#ecf0f1", font=("Helvetica", 16))
        self.label_name.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)

        self.entry_name = tk.Entry(self, font=("Helvetica", 16))
        self.entry_name.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

        self.button_login = tk.Button(self, text="Log In", command=self.login_account, bg="#2980b9", fg="white", font=("Helvetica", 16))
        self.button_login.grid(row=3, column=0, padx=10, pady=10, columnspan=2)

        self.button_back = tk.Button(self, text="Back", command=self.create_initial_window, bg="#e74c3c", fg="white", font=("Helvetica", 16))
        self.button_back.grid(row=4, column=0, padx=10, pady=10, columnspan=2)

    def account_options_window(self, account):
        self.clear_window()

        self.current_account = account

        self.button_deposit = tk.Button(self, text="Deposit", command=self.deposit_window, bg="#2980b9", fg="white", font=("Helvetica", 16))
        self.button_deposit.pack(pady=10, anchor="center")

        self.button_withdraw = tk.Button(self, text="Withdraw", command=self.withdraw_window, bg="#2980b9", fg="white", font=("Helvetica", 16))
        self.button_withdraw.pack(pady=10, anchor="center")

        self.button_balance = tk.Button(self, text="Check Balance", command=self.check_balance, bg="#2980b9", fg="white", font=("Helvetica", 16))
        self.button_balance.pack(pady=10, anchor="center")

        self.button_back = tk.Button(self, text="Back", command=self.login_account_window, bg="#e74c3c", fg="white", font=("Helvetica", 16))
        self.button_back.pack(pady=10, anchor="center")

    def deposit_window(self):
        self.transaction_window("Deposit")

    def withdraw_window(self):
        self.transaction_window("Withdraw")

    def transaction_window(self, transaction_type):
        self.clear_window()

        self.label_amount = tk.Label(self, text=f"{transaction_type} Amount:", bg="#2c3e50", fg="#ecf0f1", font=("Helvetica", 16))
        self.label_amount.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)

        self.entry_amount = tk.Entry(self, font=("Helvetica", 16))
        self.entry_amount.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        self.button_submit = tk.Button(self, text=transaction_type, command=lambda: self.perform_transaction(transaction_type), bg="#2980b9", fg="white", font=("Helvetica", 16))
        self.button_submit.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

        self.button_back = tk.Button(self, text="Back", command=lambda: self.account_options_window(self.current_account), bg="#e74c3c", fg="white", font=("Helvetica", 16))
        self.button_back.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

    def perform_transaction(self, transaction_type):
        amount = self.get_amount()
        if amount is not None:
            if transaction_type == "Deposit":
                self.current_account.deposit(amount)
                messagebox.showinfo("Info", f"Deposit successful\nNew Balance: {self.current_account.get_balance()}")
            elif transaction_type == "Withdraw":
                result = self.current_account.withdraw(amount)
                if result == "Insufficient funds":
                    messagebox.showwarning("Warning", "Insufficient funds")
                else:
                    messagebox.showinfo("Info", f"Withdrawal successful\nNew Balance: {self.current_account.get_balance()}")

    def create_account(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        address = self.entry_address.get()
        amount = self.get_amount()

        if name and phone and address and amount is not None:
            account = BankAccount(name, phone, address, amount)
            self.accounts[account.get_account_number()] = account
            messagebox.showinfo("Info", f"Account created for {name}\nAccount Number: {account.get_account_number()}\nBalance: {account.get_balance()}")
            self.create_initial_window()
        else:
            messagebox.showwarning("Warning", "Please fill out all fields and enter a valid amount")

    def login_account(self):
        account_number = self.get_account_number()
        phone = self.entry_phone.get()
        name = self.entry_name.get()

        if account_number is not None:
            account = self.accounts.get(account_number)
            if account and account.phone == phone and account.owner == name:
                self.account_options_window(account)
            else:
                messagebox.showwarning("Warning", "Account details not found or do not match")
        else:
            messagebox.showwarning("Warning", "Please enter a valid account number")

    def check_balance(self):
        details = self.current_account.get_details()
        messagebox.showinfo("Account Details", details)

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

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = BankingSystem()
    app.mainloop()
