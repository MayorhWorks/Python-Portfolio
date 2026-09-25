# Library Management System (CLI)

> **Status: in progress** — core borrowing logic is built and tested; return handling, due dates, persistence, and the menu loop are still to come.

A command-line library system written in Python, using three cooperating classes: `Book`, `Member`, and `Library`.

## Features so far

- `Book` and `Member` classes with their own data and behavior
- `Library` class that manages a catalog of books and registered members
- Borrowing a book: finds the book and member, checks availability, updates both objects
- Search books by title, search members by ID

## Still to build

- Returning a borrowed book
- Due dates and an overdue-books report
- Saving/loading data between runs
- An interactive menu

## How to Run

```bash
python library.py
```

## Requirements

- Python 3.8+

No external libraries needed.

## What I'm Learning

- Object-oriented programming: classes, `self`, constructors
- Multiple classes cooperating (`Library` calling methods on `Book` and `Member` objects it holds)
- Encapsulating data and behavior together, instead of separate functions acting on a shared list
