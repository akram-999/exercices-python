def display_menu():
    print("\nWelcome to the Final Project Menu!")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total Expenses")
    print("4. Exit")

def add_expense(expenses):
    expense_name = input("Enter the name of the expense: ")
    expense_amount = float(input("Enter the amount of the expense: $"))
    expenses[expense_name] = expense_amount
    print(f"Expense '{expense_name}' added with amount ${expense_amount:.2f}.")

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
    else:
        print("\nExpenses:")
        for name, amount in expenses.items():
            print(f"{name}: ${amount:.2f}")

def calculate_total_expenses(expenses):
    total = sum(expenses.values())
    print(f"\nTotal Expenses: ${total:.2f}")

def main():
    expenses = {}
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            calculate_total_expenses(expenses)
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
