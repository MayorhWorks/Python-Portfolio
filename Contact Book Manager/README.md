# Contact Book Manager (CLI)

A command-line contact manager written in Python.

## Features

- Add, edit, delete, and list contacts (name, phone, email, tag)
- Search contacts by name, phone, or tag — with partial, case-insensitive matching
- Prevents duplicate contacts by phone number, including when editing an existing contact
- Export all contacts to a CSV file
- Import contacts from a CSV file, automatically skipping duplicates
- Data is automatically saved to a JSON file between runs

## How to Run

```bash
python contact.py
```

## Requirements

- Python 3.8+

No external libraries needed.

## What I Learned

- Working with lists of dictionaries and mutable objects passed between functions
- Scope, parameters, and return values — including tracking a shared list across multiple functions
- Reading and writing CSV files with the `csv` module (`DictReader` / `DictWriter`)
- Nested functions and closures
- Writing docstrings and comments for readability