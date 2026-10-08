from datetime import datetime
from math import isfinite

transactions = []

def show_menu():
    """Shows the menu"""
    print("\n======= MAIN MENU =======")
    print("1. Add Transactions")
    print("2. View Transactions")
    print("3. Search Transaction")
    print("4. Exit")

def add_transaction():
    """Add transaction"""
    print("\n======= ADD NEW TRANSACTION =======")

    raw_amount = input("Amount:").strip()

    if not raw_amount:
        print("Amount can't be left empty!")
        return

    try:
        amount = float(raw_amount)
    except ValueError:
        print("Enter a valid amount e.g '12.50'")
        return

    if not isfinite(amount):
        print("Amount must be a finite number")
        return

    if amount <= 0:
        print("Amount must be greater than zero")
        return

    date = input("Date (YYYY-MM-DD): ").strip()

    if not date:
        print("Date can't be left empty!")
        return

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Enter a real date in YYYY-MM-DD format, e.g. 2026-10-08")
        return

    category = input("Category: ").strip().capitalize()
    if not category:
        print("Enter transaction Category")
        return

    transaction_type = input("Transaction type (income/expense): ").strip().lower()
    if transaction_type not in ("income", "expense"):
        print("Enter a valid transaction type")
        return 
    
    description = input("Description (optional)")  .strip()

    transaction = {
        "amount": amount,
        "date": date,
        "category": category,
        "transaction_type": transaction_type,
        "description": description
    }

    transactions.append(transaction)
    print("Transaction Added")

def view_transactions(transactions):
    """View added transactions and displays an error message if not transaction exists"""
    if not transactions:
        print("No transactions yet")
        return

    for i, transaction in enumerate(transactions, start=1):
        print(f"{i}. {transaction['transaction_type']} | {transaction['category']} | {transaction['amount']}"
              f" | {transaction['description']} | {transaction['date']}")
        

def search_transactions(transactions):
    """Search for a transaction by transaction type, amount, date"""
    def search_menu():
        print("\n ====== SEARCH TRANSACTION ======")
        print("1. Search by transaction type")
        print("2. Search by category")
        print("3. Search by Amount")
        print("4. Search by Date")
        print("5. Back to main menu")

    def print_transaction(t):
        """Print transaction in an aligned form"""
        print(f"{t['transaction_type']:<15} | {t['category']:<12} | {t['amount']:<7} | {t['description']:<12} | {t['date']:<7}")

    def search_by_type():
        """Search by transaction type"""
        transaction_type = input("Input transaction type (income/expense):").strip().lower()

        if not transaction_type:
            print("Transaction type can't be left empty")
            return

        if transaction_type not in ("income", "expense"):
            print("Enter either income or expense")
            return
        
        found = False
        for t in transactions:
            if transaction_type == t['transaction_type']:
                print_transaction(t)
                found = True

        if not found:
            print("No transaction found with this transaction type")

    def search_by_category():
        """Search by category"""
        category = input("input category: ").strip()

        if not category:
            print("Category can't be left empty")
            return

        category = category.casefold()
        found = False
        for t in transactions:
            stored_category = t['category'].casefold()
            if category in stored_category:
                print_transaction(t)
                found = True
        if not found:
            print("No transaction found in specified category")

    def search_by_amount():
        """Search by transaction amount"""
        raw_amount = input("Enter an amount to search for: ").strip()
        if not raw_amount:
            print("Amount is required to search by amount!")
            return
        try:
            amount = float(raw_amount)
        except ValueError:
            print("Enter a valid amount e.g '12.50'")
            return
        if not isfinite(amount):
            print("Amount must be a finite number")
            return
        
        if amount <= 0:
            print("Amount must be greater than 0")
            return

        found = False
        for t in transactions:
            if amount == t['amount']:
                print_transaction(t)
                found = True
        if not found:
            print("No amount found with that amount")

    def search_by_date():
        """Search by transaction date"""
        date = input("Date: (YYYY-MM-DD)").strip()
        if not date:
                print("Date can't be left empty!")
                return
        
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print("Enter a real date in YYYY-MM-DD format, e.g. 2026-10-08")
            return
        
        found = False
        for t in transactions:
            if date == t['date']:
                print_transaction(t)
                found = True
        if not found:
            print("No transaction found for this date.")
    while True:
        search_menu()
        choice = input("Choose an option (1-5)")
        if choice == "1":
            search_by_type()
        elif choice == "2":
            search_by_category()
        elif choice == "3":
            search_by_amount()
        elif choice == "4":
            search_by_date()
        elif choice == "5":
            break
        else:
            print("Invalid option")


def main():
    
    while True:
        show_menu()
        choice = input("Pick an option (1-4):")

        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_transactions(transactions)
        elif choice == "3":
            search_transactions(transactions)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("ERROR! Enter a valid option (1-4)")


if __name__ == '__main__':
    main()