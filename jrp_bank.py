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