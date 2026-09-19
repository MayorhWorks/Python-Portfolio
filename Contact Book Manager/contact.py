"""
Contact Book Manager — CLI tool

Lets a user add, edit, search, and delete contacts, with duplicate
phone-number detection and CSV import/export. Contacts persist
between runs via a local JSON file.
"""

import json
import os
import csv

DATA_FILE = "contacts.json"


# -------- Persistence ----------------


def load_contact():
    """Load the saved contacts list from DATA_FILE.

    Returns an empty list if the file doesn't exist yet, or if its
    contents are missing/corrupted.
    """
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        print("Warning: could not read contact file, starting fresh.")
        return []


def save_contact(contacts):
    """Overwrites DATA_FILE with the current contents of the contacts list."""
    with open(DATA_FILE, "w") as f:
        json.dump(contacts, f, indent=2)


def export_contacts(contacts, filename = "contacts_export.csv"):
    """Write the full contacts list to a CSV file for use externally."""
    if not contacts:
        print("No contacts to export")
        return

    with open(filename, "w", newline="") as f:  # newline="" avoids extra blank rows on Windows
        writer = csv.DictWriter(f, fieldnames=["name", "phone", "email", "tag"])
        writer.writeheader()
        writer.writerows(contacts)
        print(f"Contacts exported to {filename}")


def import_contacts(contacts, filename="contacts_export.csv"):
    """Read contacts from a CSV file and add any that aren't already saved.
    Existing contacts (matched by phone number) are skipped rather
    than duplicated. Returns the updated contacts list either way.
    """
    if not os.path.exists(filename):
        print(f"Could not find {filename}")
        return contacts
    added_count = 0
    skipped_count = 0

    with open(filename, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if phone_exist(contacts, row['phone']):
                skipped_count += 1
                continue # already saved, don't add it again
            contacts.append(row)
            added_count += 1
    save_contact(contacts)
    print(f"Imported {added_count} contact(s), skipped {skipped_count} duplicate(s).")
    return contacts


# -------- Menu display ----------------


def main_menu():
    """Prints the main menu options to the screen."""
    print("\n ======= WELCOME TO YOUR CONTACT BOOK MANAGER ======")
    print("1. Add Contact")
    print("2. List Contact")
    print("3. Edit Contact")
    print("4. Search Contact")
    print("5. Delete Contact")
    print("6. Import Contacts")
    print("7. Export Contacts")
    print("8. Exit")

def phone_exist(contacts, phone):
    """Return True if any contact in the list already has this phone number."""
    for c in contacts:
        if c['phone'] == phone:
            return True
    return False    
    

# -------- Core features ----------------


def add_contact(contacts):
    """Prompts for a new contact's details and add it to the list.
    Refuses to add if the phone number is already in use. 
    Saves to disk on success. 
    Returns the (possibly updated) contacts list.
    """
    name = input("Name: ").strip().capitalize()
    phone = input("Phone: ").strip()

    if phone_exist(contacts, phone):
        print("A contact with this phone already exists.")
        return contacts
    
    email = input("Email: ").strip()
    tag = input("tag (e.g. work/family): ").strip().lower()

    new_contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "tag": tag
    }

    contacts.append(new_contact)
    save_contact(contacts)
    print("Contact added!")
    return contacts


def list_contacts(contacts):
    """Print every saved contact, numbered, in the order they're stored."""
    print("\n ===== Your Contacts =====")
    if not contacts:
        print("No contacts added yet")
        return
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} | {contact['phone']} | {contact['email']} | {contact['tag']}")



def edit_contact(contacts):
    """Find a contact by phone number and let the user update its fields.
    Leaving a prompt blank keeps that field's current value. 
    Blocks changing the phone number to one already used by a different contact. 
    Saves to disk on success. Returns the contacts list.
    """
    phone = input("Enter Phone number to edit: ").strip()

    contact = None
    for c in contacts:
        if c["phone"] == phone:
            contact = c
            break
    if not contact:
        print("No contact found with that Phone number.")
        return contacts

    print("Leave blank to keep current value.")

    name = input(f"Name [{contact['name']}]: ").strip()
    if name:
        contact['name'] = name.capitalize()

    new_phone = input(f"Phone [{contact['phone']}]: ").strip()
    if new_phone:
        # Only block the change if it's a genuinely different number AND
        # that number already belongs to someone else.
        if new_phone != contact["phone"] and phone_exist(contacts, new_phone):
            print("Another contact already has this phone number. Keeping original.")
        else:
            contact['phone'] = new_phone

    email = input(f"Email [{contact['email']}]: ").strip()
    if email:
        contact['email'] = email

    tag = input(f"Tag [{contact['tag']}]: ").strip()
    if tag:
        contact['tag'] = tag.lower()

    save_contact(contacts)
    print("Contact updated!")
    return contacts



def search_contact(contacts):
    """Run a small sub-menu for searching contacts by name, phone, or tag.
    All three searches use partial, case-normalized matching (e.g.
    searching "jo" finds "John"). 
    Doesn't modify the contacts list.
    """
    print("\n ===== Search Contact =====")
    print("1. Search by name")
    print("2. Search by phone")
    print("3. Search by tag")
    print("4. Back to main menu")

    def print_contact(c):
        """Print one contact's fields in aligned columns."""
        print(f"{c['name']:<15} | {c['phone']:<12} | {c['email']:<25} | {c['tag']}")

    def search_by_name():
        name = input("Enter a name: ").strip().capitalize()
        found = False
        for c in contacts:
            if name in c['name']:
                print_contact(c)
                found = True
        if not found:
            print("No contact found with this name.")

    def search_by_phone():
        phone = input("Enter a phone: ").strip()
        found = False
        for c in contacts:
            if phone in c['phone']:
                print_contact(c)
                found = True
        if not found:
            print("No contact found with that phone.")

    def search_by_tag():
        tag = input("tag (e.g. work/family): ").strip().lower()
        found = False 
        for c in contacts:
            if tag in c['tag']:
                print_contact(c)
                found = True
        if not found:
            print("No contact found with that tag.")
    while True:
        choice = input("Choose an option 1-4: ")
        if choice == "1":
            search_by_name()
        elif choice == "2":
            search_by_phone()
        elif choice == "3":
            search_by_tag()
        elif choice == "4":
            break
        else:
            print("Invalid Option!")


                

def delete_contact(contacts):
    """List contacts, then remove the one the user selects by number.
    Validates the input is a real number within range before deleting.
    Saves to disk on success. 
    Returns the contacts list either way.
    """
    print("\n ===== Delete Contact =====")
    if not contacts:
        print("No contacts yet")
        return contacts
    
    list_contacts(contacts)

    user_input = input("Enter contact number to be deleted: ").strip()
    if not user_input.isdigit():
        print("Please Enter a Valid number!")
        return contacts
    number = int(user_input)

    if number < 1 or number > len(contacts):
        print("Invalid Contact number")
        return contacts

    index = number - 1 # convert the displayed 1-based number to a 0-based list index
    removed_contact = contacts.pop(index)
    print(f"Contact of '{removed_contact['name']} has been Removed")
    save_contact(contacts)
    return contacts
    
    


def menu():
    """Load saved contacts, then run the menu loop until the user exits."""
    contacts=load_contact()
    while True:
        main_menu()
        choice = input("choose an option 1-8: ")
        if choice == "1":
            contacts = add_contact(contacts)
        elif choice == "2":
            list_contacts(contacts)
        elif choice == "3":
            contacts = edit_contact(contacts)
        elif choice == "4":
            search_contact(contacts)
        elif choice == "5":
            contacts = delete_contact(contacts)
        elif choice == "6":
            contacts = import_contacts(contacts)
        elif choice == "7":
            export_contacts(contacts)
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid Choice. Please enter a valid option between 1-8")

if __name__ == "__main__":
    menu()


