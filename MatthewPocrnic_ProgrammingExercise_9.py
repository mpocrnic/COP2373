class BankAcct:
    # Initialize a new bank account with some basic info.
    def __init__(self, name, acct_number, amount, interest_rate):
        """
        Set up account holder's name, account number, initial balance,
        and the interest rate (as a percentage).
        """
        self.name = name  # Store the person's name
        self.acct_number = acct_number  # Store the account number
        self.amount = amount  # Store the starting balance
        self.interest_rate = interest_rate  # Store the annual interest rate

    # Allow the interest rate to be updated.
    def adjust_interest_rate(self, new_rate):
        """
        Change the account's interest rate.
        """
        self.interest_rate = new_rate

    # Method to add money into the account.
    def deposit(self, deposit_amount):
        """
        Add a deposit to the current balance.
        """
        if deposit_amount > 0:
            self.amount += deposit_amount  # Add to balance
        else:
            print("Deposit amount must be positive.")  # Give feedback on invalid deposit

    # Method to take money out of the account.
    def withdraw(self, withdraw_amount):
        """
        Subtract a withdrawal from the current balance.
        """
        if 0 < withdraw_amount <= self.amount:
            self.amount -= withdraw_amount  # Deduct from balance
        else:
            print("Invalid withdrawal amount.")  # Feedback if overdrawn or negative

    # Check the current account balance.
    def get_balance(self):
        """
        Show how much money is currently in the account.
        """
        return self.amount

    # Estimate interest earned over a number of days.
    def calculate_interest(self, days):
        """
        Compute the interest for a given time span.
        Formula: Interest = Principal * (Rate/100) * (Days / 365)
        """
        return self.amount * (self.interest_rate / 100) * (days / 365)

    # Define what the object should print when displayed
    def __str__(self):
        """
        Nicely format the account information for printing.
        """
        return f"Account Holder: {self.name}\n" \
               f"Account Number: {self.acct_number}\n" \
               f"Balance: ${self.amount:.2f}\n" \
               f"Interest Rate: {self.interest_rate:.2f}%"

# Function to demonstrate how the BankAcct class works
def test_bank_account():
    # Create an account for Alice with initial balance and interest rate
    account = BankAcct("Alice Smith", "12345678", 1000.00, 3.5)
    print("Initial Account Info:")
    print(account)

    # Add money to the account
    account.deposit(500.00)
    print("\nAfter depositing $500:")
    print(account)

    # Take money out
    account.withdraw(300.00)
    print("\nAfter withdrawing $300:")
    print(account)

    # Change the interest rate
    account.adjust_interest_rate(4.0)
    print("\nAfter adjusting interest rate to 4.0%:")
    print(account)

    # Calculate how much interest will be earned in 30 days
    interest = account.calculate_interest(30)
    print(f"\nInterest earned over 30 days: ${interest:.2f}")

    # Show final balance
    print(f"\nFinal balance: ${account.get_balance():.2f}")

# Run the test function only if this file is being executed directly
if __name__ == "__main__":
    test_bank_account()
