expenses=[]
def add_expense():
    name=input("Enter the name of the expense: ")
    amount=float(input("Enter the amount of the expense: "))
    expense={"name": name,
             "amount": amount}
    expenses.append(expense)
    print("Expense added successfully!")
def view_expenses():
    for expense in expenses:
        print(expense["name"], "-", expense["amount"])
def total_expenses():
    total=0
    for expense in expenses:
        total+=expense["amount"]
    print("Total=", total)
def highest_expense():
    if not expenses:
        print("No expenses recorded.")
        return
    highest=max(expenses, key=lambda x: x["amount"])
    print("Highest expense:", highest["name"], "-", highest["amount"])
while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Highest Expense")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expenses()
    elif choice == "4":
        highest_expense()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")
