import json
from pathlib import Path
from datetime import date, timedelta

DATA_FILE = Path("library_data.json")

# -------- Book ----------------
class Book:
    """Represents one book title in the library's catalog."""
    def __init__(self, title, author, isbn, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies
        self.due_date = None

    def is_available(self):
        """Return True if at least one copy of this book can be borrowed."""
        return self.copies > 0


    def borrow(self):
        """Reduce the available copies by one, if any are left."""
        if self.copies > 0:
            self.copies -= 1
            self.due_date = date.today() + timedelta(days=14)
            return True
        return False

    def return_copy(self):
           """Increase the available copies by one."""
           self.copies += 1
           self.due_date = None

    def to_dict(self):
        """Convert this book's data into a plain dictionary for saving."""
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "copies": self.copies,
            "due_date": self.due_date.isoformat() if self.due_date else None
        }

    @staticmethod
    def from_dict(data):
        """Build a Book object from a dictionary (e.g. loaded from JSON)."""
        book = Book(data["title"], data["author"], data["isbn"], data["copies"])
        if data["due_date"]:
            book.due_date = date.fromisoformat(data["due_date"])
        return book

# -------- Member ----------------
class Member:
    """Represents one library member who can borrow books."""
    def __init__(self, name, member_id):
          self.name = name
          self.member_id = member_id
          self.borrowed_books = []

    def add_borrowed_book(self, book):
          """Record that this member has borrowed a given Book object."""
          self.borrowed_books.append(book)

    def remove_book(self, book):
        """Remove a given Book object from this member's borrowed list."""
        self.borrowed_books.remove(book)

    def to_dict(self):
        """Convert this member's data into a plain dictionary for saving."""
        return {
            "name": self.name,
            "member_id": self.member_id,
            "borrowed_books": [b.to_dict() for b in self.borrowed_books]
        }
    @staticmethod
    def from_dict(data):
        """Build a Member object from a dictionary (e.g. loaded from JSON)."""
        member = Member(data["name"], data["member_id"])
        if data["borrowed_books"]:
            member.borrowed_books = [Book.from_dict(b) for b in data["borrowed_books"]]
        return member

# -------- Library ----------------

class Library:
    """Holds all books and members, and manages borrowing/returning."""
    def __init__(self):
          self.books = []
          self.members = []

    def add_book(self, book):
        """ Adds a Book object to the library's catalog."""
        self.books.append(book)

    def add_member(self, member):
         """ Adds a Member object with the library. """
         self.members.append(member)

    def find_book(self, title):
        """Search the catalog for a book matching this title."""
        for b in self.books:
            if b.title == title:
                return b
        return None

    def find_member(self, member_id):
        """Search the registered members for one matching this ID."""
        for m in self.members:
            if m.member_id == member_id:
                return m
        return None

    def borrow_book(self, title, member_id):
        """Let a member borrow a book by title, if both exist and a copy is available."""
        book = self.find_book(title)
        member = self.find_member(member_id)

        if book is None:
            print("No book found with that title.")
            return False
        
        if member is None:
            print("No member found with that ID.")
            return False
        
        if book.borrow():
            member.add_borrowed_book(book)
            print(f"{member.name} borrowed '{book.title}'.")
            return True
        else:
            print(f"No copies of '{book.title}' are available.")
            return False

    def return_book(self, title, member_id):
        """Let a member return a book by title."""
        book = self.find_book(title)
        member = self.find_member(member_id)

        if book is None:
            print("No book found with that title")
            return False
        
        if member is None:
            print("No member found with that ID.")
            return False

        if book not in member.borrowed_books:
            print(f"{member.name} does not have '{book.title}' borrowed.")
            return False

        book.return_copy()
        member.remove_book(book)
        print(f"{member.name} returned '{book.title}'.")
        return True

    def list_overdue_books(self):
        """Print every book that's currently borrowed and past its due date."""
        today = date.today()
        overdue = [b for b in self.books if b.due_date is not None and b.due_date < today]

        if not overdue:
            print("No overdue books")
            return
        
        print("\n===== Overdue Books =====")
        for b in overdue:
            print(f"{b.title} - {b.due_date}")

    def list_books(self):
        """Print every book in the catalog, with availability status."""
        if not self.books:
            print("No books in the catalog yet.")
            return
            print("\n===== Book Catalog =====")
        for b in self.books:
            status = "available" if b.is_available() else "all copies borrowed"
            print(f"{b.title} by {b.author} — {b.copies} copies ({status})")

    def to_dict(self):
        """Convert the library's catalog and members into plain dictionaries for saving."""
        return {
            "books": [b.to_dict() for b in self.books],
            "members": [m.to_dict() for m in self.members]
        }
    @staticmethod
    def from_dict(data):
        """Build a Library object from saved dictionary data."""
        library = Library()
        library.books = [Book.from_dict(b) for b in data["books"]]
        library.members = [Member.from_dict(m) for m in data["members"]]
        return library

        

# -------- Persistence ----------------

def save_library(library):
    """Save the library's full state to a JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(library.to_dict(), f, indent=4)


def load_library():
    """Load the library's state from a JSON file, or start fresh if none exists."""
    if DATA_FILE.exists():
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        return Library.from_dict(data)
    return Library()


def add_book_menu(library):
    """Prompt for a new book's details and add it to the library."""
    print("\n====== BOOK MENU ======")
    title = input("Title: ").strip()
    author = input("Author: ").strip()
    isbn = input("ISBN: ").strip()
    copies = input("Number of copies: ").strip()

    if not copies.is_digit():
        print("Copies must be a valid number.")
        return

    book = Book(title, author, isbn, int(copies))
    library.add_book(book)
    save_library(library)
    print(f"'{title}' added to the catalog.")

def add_member_menu(library):
    """Prompt for a new member's details and register them with the library."""
    print("\n===== Add Member =====")
    name = input("Name: ").strip()

    id_input = input("Member ID (a number): ").strip()
    if not id_input.isdigit():
        print("Member ID must be a valid number.")
        return
    member_id = int(id_input)

    if library.find_member(member_id):
        print("A member with that ID already exists.")
        return

    member = Member(name, member_id)
    library.add_member(member)
    save_library(library)
    print(f"'{name}' registered as member #{member_id}.")


def borrow_menu(library):
    """Prompt for a title and member ID, then attempt to borrow that book."""
    print("\n===== Borrow Book =====")
    title = input("Title: ").strip()
    id_input = input("Member ID: ").strip()
    if not id_input.isdigit():
        print("Member ID must be a valid number.")
        return
    library.borrow_book(title, int(id_input))
    save_library(library)


def return_menu(library):
    """Prompt for a title and member ID, then attempt to return that book."""
    print("\n===== Return Book =====")
    title = input("Title: ").strip()
    id_input = input("Member ID: ").strip()
    if not id_input.isdigit():
        print("Member ID must be a valid number.")
        return
    library.return_book(title, int(id_input))
    save_library(library)


def show_menu():
    print("\n======= LIBRARY MANAGEMENT SYSTEM =======")
    print("1. Add Book")
    print("2. Add Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. List Catalog")
    print("6. List Overdue Books")
    print("7. Exit")


def main():
    library = load_library()
    while True:
        show_menu()
        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            add_book_menu(library)
        elif choice == "2":
            add_member_menu(library)
        elif choice == "3":
            borrow_menu(library)
        elif choice == "4":
            return_menu(library)
        elif choice == "5":
            library.list_books()
        elif choice == "6":
            library.list_overdue_books()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-7.")


if __name__ == "__main__":
    main()


