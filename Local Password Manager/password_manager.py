entries = []

def show_menu():
    print("\n====== PASSWORD MANAGER ======")
    print("1. Add New Entry")
    print("2. View All Entries")
    print("3. Search Entry")
    print("4. Delete Entry")
    print("5. Exit")


def add_entry():
    print("\n ====== ADD NEW ENTRY ======")

    service = input("Service / Website: ").strip()
    if not service:
        print("Service cannot be empty")
        return

    username = input("Username / Email: ").strip()
    if not username:
        print("USername cannot be empty")
        return

    password = input("Password: ").strip()
    if not password:
        print("Password cannot be empty")
        return

    entry = {
        "service": service,
        "username": username,
        "password": password
    }

    entries.append(entry)
    print("Entry added successfully!")


def view_entries():
    print("\n====== ALL ENTRIES ======")
    if not entries:
        print("No entries yet")
        return

    for i, entry in enumerate(entries, start=1):
        print(f"{i}. Service: {entry['service']}")
        print(f"     Username: {entry['username']}")
        print(f"     Password: *********")
        print("=" * 30)


def main():
    while True:
        choice = input("Choose An Option (1-5): ").strip()
        if choice == 1:
            add_entry()
        elif choice == 2:
           view_entries()
        elif choice == 3:
            print("Placeholder for search entry function")
        elif choice == 4:
            print("Placeholder for delete entry function")
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-5")


if __name__ == "__main__":
    main()