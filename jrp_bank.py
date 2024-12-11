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
        self.admin_data = {
            'adminInfo': [
                {'email': 'protik@jrp.bd', 'password': '1858'},
                {'email': 'jarif@jrp.bd', 'password': '1855'},
                {'email': 'rafi@jrp.bd', 'password': '1847'}
            ]
        }
        self.loan_feature_enabled = True
        self.current_admin_email = None
        
    def login(self):
        user_email = input("> Enter your email: ")
        user_pass = input("> Enter your Password: ")
        randomNum = '0'
        for admin in self.admin_data['adminInfo']:
            if admin['email'] == user_email:
                if admin['password'] == user_pass:
                    print('>>> Logged in Successfully!')
                    self.current_admin_email = user_email  # Store the logged-in admin's email.
                    return '1'
                else:
                    print("Wrong password! Try again!")
                    randomNum = '2'
        print("User doesn't exist. Try again!")
        randomNum = '3'
        return randomNum
        
    def see_info(self):
        print(f"~~~ Currently {self.current_admin_email} is managing the bank ~~~")

    def total_bank_balance(self):
        print(f"Total bank balance: ৳ {bank.money:.2f}")

    def total_loan_amount(self):
        print(f"Total loan amount granted: ৳ {abs(user.ttl_loan):.2f}")

    def loan_feature_control(self):
        if self.loan_feature_enabled:
            self.loan_feature_enabled = False
            print("Loan feature is now turned off.")
        else:
            self.loan_feature_enabled = True
            print("Loan feature is now turned on.")

    def set_interest_rate(self):
        try:
            rate = float(input("> Enter new interest rate (as %): "))
            if rate < 0:
                raise ValueError("Interest rate cannot be negative.")
            bank.interest_rate = rate
            print(f"Interest rate updated to {rate:.2f}%")
        except ValueError as e:
            print(f"Error: {e}")


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
        self.current_user_email = ""
        self.user_data = {}
        self.ttl_loan = 0.0

    def see_info(self):
        print(f"~~~ Currently {self.current_user_email} is logged in with Taka ৳ {self.user_data[self.current_user_email]['balance']:.2f} ~~~")
        
    def login(self):
        user_email = input("> Enter your email: ")
        user_pass = input("> Enter your Password: ")
        if user_email in self.user_data:
            if(self.user_data[user_email]['password'] == user_pass):
                print('>>> Logged in Successfully!')
                self.current_user_email = user_email
                return '1'
            print("Wrong password! Try again!")
            return '2'
        print("User don't exist. Try creating one tapping 3!")
        return '3'
            

    def create_account(self):
        user_email = input("> Enter your Email: ").strip().lower()
        user_pass = input("> Enter your Password: ").strip()
        initial_balance = 0
        self.user_data[user_email] = {'password': user_pass, 'balance': initial_balance, 'transactions': []}
        print(f"~~~ Account created for {user_email} successfully ~~~")

    def check_balance(self):
        print(f"~~~ Your current balance is: ৳ {self.user_data[self.current_user_email]['balance']:.2f} ~~~")

    def deposit_money(self):
            try:
                amount = float(input("> Enter the amount to deposit: "))
                if amount < 0:
                    raise ValueError("Please enter a non-negative amount.")
                self.user_data[self.current_user_email]['balance'] += amount
                bank.money += amount
                self.user_data[self.current_user_email]['transactions'].append(Transaction(self.current_user_email, amount, "Deposit"))
                print(f"~~~ ৳ {amount:.2f} deposited successfully. Current balance: ৳ {self.user_data[self.current_user_email]['balance']:.2f} ~~~")
            except ValueError as e:
                print(f"Error: {e}")

    def withdraw_money(self):
            try:
                amount = float(input("> Enter the amount to withdraw: "))
                if amount < 0:
                    raise ValueError("Please enter a non-negative amount.")
                if amount <= self.user_data[self.current_user_email]['balance']:
                    self.user_data[self.current_user_email]['balance'] -= amount
                    bank.money -= amount
                    self.user_data[self.current_user_email]['transactions'].append(Transaction(self.current_user_email, amount, "Withdrawal"))
                    print(f"৳ {amount:.2f} withdrawn successfully. Current balance: ৳ {self.user_data[self.current_user_email]['balance']:.2f}")
                else:
                    raise ValueError("Insufficient balance.")
            except ValueError as e:
                print(f"Error: {e}")

    def transaction_history(self):
            print(f">>> Transaction history for {self.current_user_email}:")
            transactions = self.user_data[self.current_user_email]['transactions']
            for i, transaction in enumerate(transactions, start=1):
                print(f"{i}. {transaction}")

    def take_loan(self):
        if admin.loan_feature_enabled:
                try:
                    loan_amount = float(input("> Enter loan amount: "))
                    if loan_amount < 0:
                        raise ValueError("Loan amount must be positive.")
                    if loan_amount <= bank.money:
                        if loan_amount <= (self.user_data[self.current_user_email]['balance'] * 2):
                            self.user_data[self.current_user_email]['balance'] += loan_amount
                            bank.money -= loan_amount
                            self.ttl_loan += loan_amount
                            self.user_data[self.current_user_email]['transactions'].append(Transaction(self.current_user_email, loan_amount, "Loan"))
                            print(f"Loan granted! New balance: ৳{self.user_data[self.current_user_email]['balance']:.2f}")
                        else:
                            raise ValueError("Loan exceeds allowed limit.")
                    else:
                        print("Bank has insufficient funds.")
                except ValueError as e:
                    print(f"Error: {e}")
        else:
            print("!!! Loan feature is disabled by admin.")
        
    def apply_interest(self):
            balance = self.user_data[self.current_user_email]['balance']
            if balance > 0:
                try:
                    time = float(input("> Enter the time period (in years): "))
                    interest = bank.calculate_interest(balance, bank.interest_rate, time)
                    self.user_data[self.current_user_email]['balance'] += interest
                    bank.money += interest
                    self.user_data[self.current_user_email]['transactions'].append(f"Applied interest of ৳ {interest:.2f} for {time} years")
                    print(f"~~~ Interest of ৳ {interest:.2f} applied. Current balance: ৳ {self.user_data[self.current_user_email]['balance']:.2f} ~~~")
                except ValueError as e:
                    print(f"Error: {e}")
            else:
                print("~~~ Interest can only be applied to positive balances. ~~~")
            
            
class Bank:
    def __init__(self):
        self.money = 10000000000
        self.interest_rate = 5.0
    def calculate_interest(self, principal, rate, time):
        return (principal * rate * time) / 100


def main():
    while True:
        print("\n******** JRP Bank ********")
        print("1. User Options")
        print("2. Admin Options")
        print("3. Create User Account")
        print("4. Bank Reports")
        print("5. Quit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            handle_user_options()
        elif choice == "2":
            handle_admin_options()
        elif choice == "3":
            user.create_account()
        elif choice == "4":
            report.generate_report(user)
        elif choice == "5":
            print("Thank you for using JRP Bank!")
            break
        else:
            print("Invalid choice! Please try again.")

def handle_user_options():
    while True:
        login_status = user.login()
        if login_status == '2': 
            continue
        elif login_status == '3':
            return
        elif login_status == '1':
            while True:
                print("\n**** User Options ****")
                print("1. Deposit Money")
                print("2. Withdraw Money")
                print("3. Check Balance")
                print("4. Transaction History")
                print("5. Take Loan")
                print("6. Apply Interest")
                print("7. User Info")
                print("8. Log Out")
                user_choice = input("> Enter your choice: ")
                
                if user_choice == "1":
                    user.deposit_money()
                elif user_choice == "2":
                    user.withdraw_money()
                elif user_choice == "3":
                    user.check_balance()
                elif user_choice == "4":
                    user.transaction_history()
                elif user_choice == "5":
                    user.take_loan()
                elif user_choice == "6":
                    user.apply_interest()
                elif user_choice == "7":
                    user.see_info()
                elif user_choice == "8":
                    return
                else:
                    print("Invalid choice! Please try again.")

def handle_admin_options():
    while True:
        login_status = admin.login()
        if login_status == '2': 
            continue
        elif login_status == '3':
            return
        elif login_status == '1':
            print("\n**** Admin Options ****")
            print("1. Total Bank Balance")
            print("2. Total Loan Amount")
            print("3. Set Interest Rate")
            print("4. Loan Feature Toggle")
            print("5. Admin Info")
            print("6. Log Out")
            while True:
                admin_choice = input("> Enter your choice: ")
                if admin_choice == "1":
                    admin.total_bank_balance()
                elif admin_choice == "2":
                    admin.total_loan_amount()
                elif admin_choice == "3":
                    admin.set_interest_rate()
                elif admin_choice == "4":
                    admin.loan_feature_control()
                elif admin_choice == "5":
                    admin.see_info()
                elif admin_choice == "6":
                    return
                else:
                    print("Invalid choice! Please try again.")
        


if __name__ == "__main__":
    admin = Admin()
    user = User()
    bank = Bank()
    report = BankReport()
    main()
