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
        try:
            user_email = input("> Enter your Email: ").strip()
            if user_email in self.user_data:
                print(f"~~~ Your current balance is: ৳ {self.user_data[user_email]['balance']:.2f} ~~~")
            else:
                raise ValueError("User not found")
        except ValueError as e:
            print(f"Error: {e}")

    def deposit_money(self):
        user_email = input("> Enter your Email: ").strip()
        if user_email in self.user_data:
            try:
                amount = float(input("> Enter the amount to deposit: "))
                if amount < 0:
                    raise ValueError("Please enter a non-negative amount.")
                self.user_data[user_email]['balance'] += amount
                bank.money += amount
                self.user_data[user_email]['transactions'].append(f"Deposited ৳ {amount:.2f}")
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
                    self.user_data[user_email]['transactions'].append(f"Withdrew ৳{amount:.2f}")
                    print(f"৳{amount:.2f} withdrawn successfully. Current balance: ৳{self.user_data[user_email]['balance']:.2f}")
                else:
                    raise ValueError("Insufficient balance")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("~~~ User not found. ~~~")

    def transaction_history(self):
        user_email = input("Enter your Email: ").strip()
        if user_email in self.user_data:
            print(f">>> Transaction history for {user_email}:")

            transactions = self.user_data[user_email]['transactions']
            deposits = []
            withdrawals = []

            for transaction in transactions:
                if "Deposited" in transaction:
                    amount = float(transaction.split("৳")[1].strip())
                    deposits.append(amount)
                elif "Withdrew" in transaction:
                    amount = float(transaction.split("৳")[1].strip())
                    withdrawals.append(amount)

            avg_transacted = np.mean(deposits + withdrawals) if deposits or withdrawals else 0
            avg_withdrawn = np.mean(withdrawals) if withdrawals else 0

            for i, transaction in enumerate(transactions, start=1):
                print(f"{i}. {transaction}")

            print(f"\n>>> Average Transacted Money: ৳ {avg_transacted:.2f}")
            print(f">>> Average Withdrawn Money: ৳ {avg_withdrawn:.2f}")
        else:
            print("~~~ User not found. ~~~")

    def take_loan(self):
        if admin.admin_data['admin']['loan_feature_enabled']:
            user_email = input("Enter your Email: ").strip()
            try:
                loan_amount = float(input("Enter the amount of loan you want to take: "))
                if loan_amount < 0:
                    raise ValueError("Please enter a non-negative loan amount.")
                if user_email in self.user_data and loan_amount <= bank.money:
                    if self.user_data[user_email]['balance'] > 0 and loan_amount <= (self.user_data[user_email]['balance'] * 2):
                        self.ttl_loan += loan_amount
                        self.user_data[user_email]['balance'] += loan_amount
                        bank.money -= loan_amount
                        self.user_data[user_email]['transactions'].append(f"Took a loan of ৳ {loan_amount:.2f}")
                        print(f"Loan of ৳ {loan_amount:.2f} granted. Current balance: ৳ {self.user_data[user_email]['balance']:.2f}")
                    else:
                        raise ValueError("Loan exceeds twice the balance or insufficient bank funds")
                else:
                    raise ValueError("User not found or bank is bankrupt")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("!!! Loan feature is disabled by admin.")


class Bank:
    def __init__(self):
        self.money = 10000000000

    def calculate_interest(self, principal, rate, time):
        interest = lambda p, r, t: (p * r * t) / 100
        return interest(principal, rate, time)


def main():
    while True:
        print("\n******** JRP Bank ********")
        print("1. User Options")
        print("2. Admin Options")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\n**** User Options ****")
            print("1. Create Account")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Check Balance")
            print("5. Transaction History")
            print("6. Take Loan")
            print("7. Go Back")
            uo_c = input("Enter: ")
            if uo_c == "1":
                user.create_account()
            elif uo_c == "2":
                user.deposit_money()
            elif uo_c == "3":
                user.withdraw_money()
            elif uo_c == "4":
                user.check_balance()
            elif uo_c == "5":
                user.transaction_history()
            elif uo_c == "6":
                user.take_loan()
            elif uo_c == "7":
                continue
        elif choice == "2":
            print("\n**** Admin Options ****")
            print("1. Create Account")
            print("2. Total Bank Balance")
            print("3. Total Loan Amount")
            if admin.admin_data['admin']['loan_feature_enabled']:
                print("4. Loan Feature on/off (currently on)")
            else:
                print("4. Loan Feature on/off (currently off)")
            print("5. Go Back")
            ad_c = input("Enter: ")
            if ad_c == "1":
                admin.create_account()
            elif ad_c == "2":
                admin.total_bank_balance()
            elif ad_c == "3":
                admin.total_loan_amount()
            elif ad_c == "4":
                admin.loan_feature_control()
            elif ad_c == "5":
                continue
        elif choice == "3":
            break

    print("\nThanks For Visiting JRP Bank")


if __name__ == "__main__":
    admin = Admin()
    user = User()
    bank = Bank()
    main()
