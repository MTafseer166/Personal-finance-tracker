# Personal Finance Tracker

A console-based personal finance tracker written in Python.

**Final Project — Option 2: Personal Finance / Expense Management System**

## What It Does

This program lets you record your income and expenses, see where your money goes, and check how much you have left. All data is saved to a CSV file, so nothing is lost when you close the program.

## Features

- Add income (source, amount, description)
- Add expense (category, amount, description)
- View all transactions in one table
- Search transactions by category
- Show a summary: total income, total expenses, remaining balance
- Analyze expenses by category using Pandas (shows which category you spend the most on)
- Delete a transaction
- Input validation (no negative or zero amounts, no empty category/source)
- Data automatically saved to `transactions.csv`

## Concepts Used

Functions, lists, dictionaries, file handling (CSV reading/writing), conditional statements, loops, exception handling (`try`/`except`), and Pandas (`DataFrame`, `groupby`) for the expense analysis.

## Requirements

```bash
pip install pandas
```

## How to Run

```bash
python finance_tracker.py
```

`transactions.csv` is created automatically the first time you add a transaction.

## Menu

```
===== Personal Finance Tracker =====
1. Add Income
2. Add Expense
3. View All Transactions
4. Search by Category
5. Show Summary (Income, Expenses, Balance)
6. Analyze Expenses by Category
7. Delete Transaction
8. Exit
```

## How It Works (short explanation)

- Every income or expense is stored as a dictionary with four fields: `type`, `category`, `amount`, `description`.
- All transactions are kept in a list in memory while the program runs.
- `save_transactions()` writes the whole list to `transactions.csv` every time something changes, so the file always matches what's on screen.
- `load_transactions()` reads that file back in when the program starts, so your data is still there the next time you run it.
- The summary adds up all `Income` type amounts and all `Expense` type amounts separately, then subtracts to get the balance.
- The analysis feature loads the expenses into a Pandas DataFrame and uses `groupby("category")` to total up spending per category.

