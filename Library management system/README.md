# Library Management System (CLI)

A command-line library system written in Python, using three cooperating classes: `Book`, `Member`, and `Library`.

## Features

- `Book`, `Member`, and `Library` classes, each handling their own data and behavior
- Add books to the catalog and register members
- Borrow and return books, with automatic 14-day due dates
- Prevents borrowing when no copies are available, and returning a book that isn't actually checked out
- Overdue books report, comparing due dates against today's date
- Full catalog listing showing availability per book
- Data persists between runs via JSON — including due dates and which member has which book

## How to Run

```bash
python library.py
```

## Requirements

- Python 3.8+

No external libraries needed.

## What I Learned

- Object-oriented programming: classes, `self`, constructors, and multiple classes cooperating together
- The difference between a class (the blueprint) and an object/instance (a specific thing built from it)
- `@staticmethod` for building objects from saved data
- Converting objects to and from plain dictionaries (`to_dict()` / `from_dict()`) to make them JSON-serializable, including nested objects (a `Member`'s borrowed `Book` objects)
- Working with `date` and `timedelta` for due-date calculations and comparisons
- Structuring a larger, multi-class program compared to the single-flat-list approach used in earlier projects
