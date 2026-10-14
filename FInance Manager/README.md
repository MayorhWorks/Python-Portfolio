# Personal Finance Manager

A beginner-friendly command-line Python project for recording and reviewing personal income and expenses.

## Project goals

The long-term goal is to grow this program into a multi-file finance application that can:

- Record, organize, search, and manage transactions.
- Calculate balances and generate monthly or yearly reports.
- Set budgets and compare them with expenses.
- Save and load information between runs.
- Separate menus, transaction logic, reports, and data storage into modules as the project grows.

## Completed

- Command-line menu for adding, viewing, searching, summarizing, and deleting transactions.
- Add transactions with an amount, date, category, transaction type, and optional description.
- Validate that amounts are numeric, finite, and greater than zero.
- Validate dates with the `YYYY-MM-DD` format.
- Search by transaction type, category, amount, or date.
- Display transactions in a numbered list.
- Display total income, total expenses, and balance in a formatted summary.
- Save transactions to and load them from a JSON file.
- Save the updated transaction list after adding or deleting a transaction.

## In progress

- Edit an existing transaction. The edit workflow and amount/date updates have been started; menu integration and the remaining editable fields still need to be completed.

## Planned

- Complete transaction editing, including validation for every editable field.
- Add monthly/yearly reports and spending totals by category.
- Add category budgets and compare them with expenses.
- Improve data-file error handling and monetary amount precision.
- Split the program into multiple Python files as it grows.

## Data file

The program creates `transactions.json` beside `main.py` to store transaction data between runs. Treat this as local personal data; do not commit real financial records to a public repository.

## Run the program

From this folder, run:

```text
python main.py
```
