
import json
from pathlib import Path
DATA_FILE = Path("expenses.json")


def save_expenses():
    """Write the current expenses list to a JSON file."""
    with open (DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(expenses, f, indent=4)



def load_expenses():
    """Load expenses from the JSON file if it exists."""
    global expenses
    if DATA_FILE.exists():
        with open (DATA_FILE, "r", encoding="utf-8") as f:
            expenses = json.load(f)
    else:
        expenses = []



expenses = []  # list of dictionaries: {"amount": float, "category": str, "note": str}

def show_menu():
    print("\n ===== Personal Expense Tracker=====")
    print("1. Add Expense")
    print("2. List Expenses")
    print("3. Show Totals")
    print("4. View monthly totals")
    print("5. Exit")
    print("=" * 15)


def add_expense():
    print("\n ==== Add New Expense ====")

    while True:
        amount_str = input("Amount: ").strip()
        try:
            amount=float(amount_str)
            if amount <= 0:
                print("Amount must be greater than zero. Try again!")
                continue
            break
        except ValueError:
            print("Please enter a valid number (example: 12.50)")

    category = input("Category(e.g Transport, Food, Rent...): ").strip()
    description = input("Description: ").strip()
    date = input("Date (YYYY-MM-DD): ").strip()

    expense = {
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    }

    expenses.append(expense)
    print(f"Expense of {amount:.2f} added successfully!")
    save_expenses()

    
def list_expenses():
    print("\n==== All Expenses ====")
    if not expenses:
        print("No Expenses Recorded Yet")
        return
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['date']} | {expense['category']:12} |"
              f"{expense['amount']:8.2f} | {expense['description']}")
        

def show_category_totals():
    print("\n ==== Category Totals ==== ")

    if not expenses:
        print("No Expenses Recorded Yet")
        return
    totals = {}

    for expense in expenses:

        category = expense["category"]
        amount = expense["amount"]

        if category in totals:
            totals[category] += amount
        else:
            totals[category] = amount

    for category, total in totals.items():
        print(f"{category:15} : {total:8.2f}")


def show_monthly_totals():
    print("\n ==== Monthly Totals ==== ")

    if not expenses: 
        print("No Expenses Recorded Yet")
        return

    total = {}

    for expense in expenses:

        month = expense["date"][:7]
        amount = expense["amount"]

        if month in total:
            total[month] += amount
        else:
            total[month] = amount

    for month in sorted(total.keys()):
        print(f"{month} : {total[month]:8.2f}")



def main():
    load_expenses()
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            list_expenses()
        elif choice == "3":
            show_category_totals()
        elif choice == "4":
            show_monthly_totals()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1,2,3, or 4. ")

if __name__ == "__main__":
    main()