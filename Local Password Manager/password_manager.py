"""
Local Password Manager (CLI)

A simple command-line password manager that stores
service, username and encrypted password.
Data is saved permanently using JSON + Fernet encryption.
"""

import json 
from pathlib import Path
from cryptography.fernet import Fernet

# ---------- File paths ----------

DATA_FILE = Path("passwords.json") # Stores the encrypted entries
KEY_FILE = Path("secret.key") # Stores the encryption key

# Main list that holds all password entries
entries = []

# ---------- Save / Load ----------

def save_entries():
    """Save all entries to a JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(entries, f, indent=4)


def load_entries():
    """Load entries from the JSON file if it exists."""
    global entries
    if DATA_FILE.exists():
        with open(DATA_FILE, "r", encoding= "utf-8") as f:
            entries = json.load(f)
    else:
        entries = []


# ---------- Encryption helpers ----------

def generate_key():
    """Generate a new encryption key and save it to a file."""
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)
    return key


def load_key():
    """Load the key from file, or create a new one if it doesn't exist."""
    if KEY_FILE.exists():
        with open(KEY_FILE, "rb") as f:
            return f.read()
    else:
        return generate_key()


def encrypt_password(password: str, key: bytes) -> str:
    """Encrypt a plain password and return it as a string."""
    f = Fernet(key)
    encrypted = f.encrypt(password.encode())
    return encrypted.decode()


def decrypt_password(encrypted_password: str, key: bytes) -> str:
    """Decrypt an encrypted password."""
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_password.encode())
    return decrypted.decode()


# ---------- Menu ----------

def show_menu():
    """Display the main menu"""
    print("\n====== PASSWORD MANAGER ======")
    print("1. Add New Entry")
    print("2. View All Entries")
    print("3. Search Entry")
    print("4. Delete Entry")
    print("5. Exit")

# ---------- Core features ----------

def add_entry():
    """Ask the user for service, username and password, then encrypt & save"""
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
    # Encrypt the password before storing
    key = load_key()
    encrypted_pw = encrypt_password(password, key)

    entry = {
        "service": service,
        "username": username,
        "password": encrypted_pw
    }

    entries.append(entry)
    print("Entry added successfully!")
    save_entries()


def view_entries():
    """Show all entries with passwords hidden"""
    print("\n====== ALL ENTRIES ======")
    if not entries:
        print("No entries yet")
        return

    for i, entry in enumerate(entries, start=1):
        print(f"{i}. Service: {entry['service']}")
        print(f"     Username: {entry['username']}")
        print(f"     Password: *********")
        print("=" * 30)

def search_entry():
    """Search for entries by service name (case-insensitive)"""
    print("\n ====== SEARCH ENTRY ======")
    if not entries:
        print("No entries yet")
        return
    prompt = input("Enter service name to search: ").strip().lower()

    if not prompt:
        print("Search cannot be left empty.")
        return

    found = False

    for i, entry in enumerate(entries, start = 1):
        if prompt in entry["service"].lower():
            print(f"\n {i}. Service : {entry['service']:12}")
            print(f"       Username : {entry['username']}")
            print(f"       Password: **********")
            found = True

    if not found:
        print("No matching item found.")


def delete_entry():
    """Delete an entry by its number"""
    print("\n ====== DELETE ENTRY ======")
    if not entries:
        print("No entries yet")
        return

    # Show current entries so the user can see the numbers
    view_entries()

    prompt = input("\n Enter the number of the entry to delete. ").strip()

    if not prompt.isdigit():
        print("Please enter a valid number.")
        return

    number = int(prompt)

    if number < 1 or number > len(entries):
        print("Please enter a valid number")
        return

    index = number - 1
    removed = entries.pop(index)
    print(f"Entry for '{removed['service']}' has been deleted")
    save_entries()

# ---------- Main program ----------

def main():
    """Start the application"""
    load_entries() # Load existing data when the program starts
    while True:
        show_menu()
        choice = input("Choose An Option (1-5): ").strip()
        if choice == "1":
            add_entry()
        elif choice == "2":
           view_entries()
        elif choice == "3":
            search_entry()
        elif choice == "4":
            delete_entry()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-5")


if __name__ == "__main__":
    main()