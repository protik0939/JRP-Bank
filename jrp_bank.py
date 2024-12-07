#JRP Bank
import numpy as np

class Person:
    def __init__(self, email):
        self.email = email

    def __str__(self):
        return f"Email: {self.email}"


class Admin(Person):
    def __init__(self):
        super().__init__(email="admin@bank.com")
        self.admin_data = {'admin': {'Email': self.email, 'loan_feature_enabled': True}}

    def total_bank_balance(self):
        print(f"Total bank balance: ৳ {bank.money:.2f}")

    def total_loan_amount(self):
        print(f"Total loan amount granted: ৳ {abs(user.ttl_loan):.2f}")

    def loan_feature_control(self):
        if self.admin_data['admin']['loan_feature_enabled']:
            self.admin_data['admin']['loan_feature_enabled'] = False
            print("Loan feature is now turned off.")
        else:
            self.admin_data['admin']['loan_feature_enabled'] = True
            print("Loan feature is now turned on.")

    def create_account(self):
        admin_email = input("> Enter Admin Name: ").strip().lower()
        self.admin_data['admin']['Email'] = admin_email
        print(f"Account created for {admin_email}, a new employee for our bank.")
        
        
    def set_interest_rate(self):
        try:
            rate = float(input("> Enter new interest rate (as %): "))
            if rate < 0:
                raise ValueError("Interest rate cannot be negative.")
            bank.interest_rate = rate
            print(f"Interest rate updated to {rate:.2f}%")
        except ValueError as e:
            print(f"Error: {e}")



#  Rafi            


class Transaction:
    def __init__(self, user_email, amount, transaction_type):
        self.user_email = user_email
        self.amount = amount
        self.transaction_type = transaction_type.lower().strip()
        self.description = f"{transaction_type} of ৳{amount:.2f}"

    def __str__(self):
        return f"Transaction for {self.user_email}: {self.description}"


class BankReport:
    def __init__(self):
        self.report_data = []

    def generate_report(self, users):
        total_users = len(users.user_data)
        total_balance = np.sum([user['balance'] for user in users.user_data.values()])
        print("\n>>> Bank Report <<<")
        print(f"Total Users: {total_users}")
        print(f"Total Bank Balance: ৳{total_balance:.2f}\n")


class LoanManager(Person):
    def __init__(self):
        super().__init__(email="")
        self.ttl_loan = 0.0

    def calculate_interest(self, principal, rate, time):
        return (principal * rate * time) / 100


class User(Person):
    def __init__(self):
        super().__init__(email="")
        self.user_data = {}
        self.ttl_loan = 0.0

    def create_account(self):
        user_email = input("> Enter your Email: ").strip().lower()
        initial_balance = 0
        self.user_data[user_email] = {'balance': initial_balance, 'transactions': []}
        print(f"~~~ Account created for {user_email} successfully ~~~")

    def check_balance(self):
        user_email = input("> Enter your Email: ").strip()
        if user_email in self.user_data:
            print(f"~~~ Your current balance is: ৳ {self.user_data[user_email]['balance']:.2f} ~~~")
        else:
            print("~~~ User not found ~~~")

    def deposit_money(self):
        user_email = input("> Enter your Email: ").strip()
        if user_email in self.user_data:
            try:
                amount = float(input("> Enter the amount to deposit: "))
                if amount < 0:
                    raise ValueError("Please enter a non-negative amount.")
                self.user_data[user_email]['balance'] += amount
                bank.money += amount
                self.user_data[user_email]['transactions'].append(Transaction(user_email, amount, "Deposit"))
                print(f"~~~ ৳ {amount:.2f} deposited successfully. Current balance: ৳ {self.user_data[user_email]['balance']:.2f} ~~~")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("~~~ User not found. ~~~")

    def withdraw_money(self):
        user_email = input("> Enter your Email: ").strip()
        if user_email in self.user_data:
            try:
                amount = float(input("> Enter the amount to withdraw: "))
                if amount < 0:
                    raise ValueError("Please enter a non-negative amount.")
                if amount <= self.user_data[user_email]['balance']:
                    self.user_data[user_email]['balance'] -= amount
                    bank.money -= amount
                    self.user_data[user_email]['transactions'].append(Transaction(user_email, amount, "Withdrawal"))
                    print(f"৳ {amount:.2f} withdrawn successfully. Current balance: ৳ {self.user_data[user_email]['balance']:.2f}")
                else:
                    raise ValueError("Insufficient balance.")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("~~~ User not found. ~~~")

    def transaction_history(self):
        user_email = input("> Enter your Email: ").strip()
        if user_email in self.user_data:
            print(f">>> Transaction history for {user_email}:")
            transactions = self.user_data[user_email]['transactions']
            for i, transaction in enumerate(transactions, start=1):
                print(f"{i}. {transaction}")
        else:
            print("~~~ User not found. ~~~")

    def take_loan(self):
        if admin.admin_data['admin']['loan_feature_enabled']:
            user_email = input("> Enter your Email: ").strip()
            if user_email in self.user_data:
                try:
                    loan_amount = float(input("> Enter loan amount: "))
                    if loan_amount < 0:
                        raise ValueError("Loan amount must be positive.")
                    if loan_amount <= bank.money:
                        if loan_amount <= (self.user_data[user_email]['balance'] * 2):
                            self.user_data[user_email]['balance'] += loan_amount
                            bank.money -= loan_amount
                            self.ttl_loan += loan_amount
                            self.user_data[user_email]['transactions'].append(Transaction(user_email, loan_amount, "Loan"))
                            print(f"Loan granted! New balance: ৳{self.user_data[user_email]['balance']:.2f}")
                        else:
                            raise ValueError("Loan exceeds allowed limit.")
                    else:
                        print("Bank has insufficient funds.")
                except ValueError as e:
                    print(f"Error: {e}")
            else:
                print("~~~ User not found. ~~~")
        else:
            print("!!! Loan feature is disabled by admin.")
        
    def apply_interest(self):
        user_email = input("> Enter your Email: ").strip()
        if user_email in self.user_data:
            balance = self.user_data[user_email]['balance']
            if balance > 0:
                try:
                    time = float(input("> Enter the time period (in years): "))
                    interest = bank.calculate_interest(balance, bank.interest_rate, time)
                    self.user_data[user_email]['balance'] += interest
                    bank.money += interest
                    self.user_data[user_email]['transactions'].append(f"Applied interest of ৳ {interest:.2f} for {time} years")
                    print(f"~~~ Interest of ৳ {interest:.2f} applied. Current balance: ৳ {self.user_data[user_email]['balance']:.2f} ~~~")
                except ValueError as e:
                    print(f"Error: {e}")
            else:
                print("~~~ Interest can only be applied to positive balances. ~~~")
        else:
            print("~~~ User not found. ~~~")