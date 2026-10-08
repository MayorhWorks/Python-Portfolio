# Personal Finance Manager

A command-line Python project for recording and reviewing personal income and expenses.

## Project goals

The long-term goal is a multi-file finance application that can:

- Record, organize, search, and manage transactions.
- Calculate balances and generate monthly or yearly reports.
- Set budgets and compare them with expenses.
- Save and load information between runs.
- Grow into a structured project with separate modules for menus, transaction logic, reports, and data storage.

## Completed so far

- Command-line menu for adding, viewing, searching, and exiting.
- Add transactions with amount, date, category, type, and optional description.
- Validate that amounts are numeric, finite, and greater than zero.
- Validate dates using the `YYYY-MM-DD` format.
- Search transactions by type, category, amount, or date.
- Display transactions in a numbered list.

Transactions are currently kept in memory, so they are lost when the program closes.

## Planned next

- Save and load transactions using JSON.
- Add balance and spending reports.
- Add category budgets.
- Split the program into multiple Python files as the project grows.

## Run the program

From this folder, run:

```text
python main.py
```
