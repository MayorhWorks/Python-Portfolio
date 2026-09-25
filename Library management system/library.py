class Book:
    def __init__(self, title, author, isbn, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies

    def is_available(self):
        """Return True if at least one copy of this book can be borrowed."""
        return self.copies > 0


    def borrow(self):
        """Reduce the available copies by one, if any are left."""
        if self.copies > 0:
            self.copies -= 1
            return True
        return False

    def return_copy(self):
           """Increase the available copies by one."""
           self.copies += 1

harry_potter = Book("Harry Potter", "J.K. Rowling", "978-0439708180", 3)

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

alice = Member("Alice", 1)

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

library = Library()
library.add_book(harry_potter)
library.add_member(alice)

library.borrow_book("Harry Potter", 1)
print(harry_potter.copies)
print(alice.borrowed_books)

     


     

