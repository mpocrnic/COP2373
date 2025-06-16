# Import the reduce function to help with combining values in a list
from functools import reduce

# Function to collect expenses from the user
def get_expenses():
    # Initialize an empty list to store expense entries
    expenses = []
    
    # Give the user instructions on how to enter expenses
    print("Enter your monthly expenses. Type 'done' when finished.")
    
    # Start a loop to collect expense type and amount from the user
    while True:
        # Ask for the type or name of the expense
        expense_type = input("Enter the type of expense (or 'done' to finish): ")
        
        # If the user types 'done', stop asking for more expenses
        if expense_type.lower() == 'done':
            break
        
        # Ask for the amount of that expense
        try:
            amount = float(input(f"Enter the amount for {expense_type}: "))
            # Store the expense as a tuple (type, amount)and handle cases where the user does not enter a valid number
            expenses.append((expense_type, amount))
        except ValueError:
            print("Invalid amount. Please enter a number.")
    
    # Return the list of all expenses entered by the user
    return expenses

# Main function that runs the program
def main():
    # Get the list of expenses from the user
    expenses = get_expenses()

    if not expenses:
        print("No expenses entered.")
        return

    # Find the total of all expenses using reduce
    total = reduce(lambda acc, expense: acc + expense[1], expenses, 0)

    # Find the expense with the highest amount using reduce
    highest = reduce(lambda acc, expense: expense if expense[1] > acc[1] else acc, expenses)

    # Find the expense with the lowest amount using reduce
    lowest = reduce(lambda acc, expense: expense if expense[1] < acc[1] else acc, expenses)

    # Display the results in a friendly, easy-to-read format
    print("\nExpense Summary:")
    print(f"Total Expense: ${total:.2f}")
    print(f"Highest Expense: {highest[0]} - ${highest[1]:.2f}")
    print(f"Lowest Expense: {lowest[0]} - ${lowest[1]:.2f}")

# Run the main function when the program starts
if __name__ == "__main__":
    main()
