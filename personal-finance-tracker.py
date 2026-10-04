import csv
import os
import pandas as pd

FILE_NAME = "transactions.csv"
FIELDS = ["type", "category", "amount", "description"]


def load_transactions():
    transactions = []
    if not os.path.exists(FILE_NAME):
        return transactions

    file = open(FILE_NAME, "r", newline="")
    reader = csv.DictReader(file)
    for row in reader:
        transactions.append({
            "type": row["type"],
            "category": row["category"],
            "amount": float(row["amount"]),
            "description": row["description"],
        })
    file.close()
    return transactions


def save_transactions(transactions):
    file = open(FILE_NAME, "w", newline="")
    writer = csv.DictWriter(file, fieldnames=FIELDS)
    writer.writeheader()
    writer.writerows(transactions)
    file.close()

    def get_amount():
    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return None
        return amount
    except ValueError:
        print("Invalid amount.")
        return None

def get_amount():
    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return None
        return amount
    except ValueError:
        print("Invalid amount.")
        return None

def add_income(transactions):
    print("\n--- Add Income ---")
    category = input("Enter source (e.g. Salary, Freelance): ").strip()
    if category == "":
        print("Source cannot be empty.")
        return
    amount = get_amount()
    if amount is None:
        return
    description = input("Enter description (optional): ").strip()

    transactions.append({
        "type": "Income",
        "category": category,
        "amount": amount,
        "description": description,
    })
    save_transactions(transactions)
    print("Income added successfully!")

def add_expense(transactions):
    print("\n--- Add Expense ---")
    category = input("Enter category (e.g. Food, Rent, Transport): ").strip()
    if category == "":
        print("Category cannot be empty.")
        return
    amount = get_amount()
    if amount is None:
        return
    description = input("Enter description (optional): ").strip()

    transactions.append({
        "type": "Expense",
        "category": category,
        "amount": amount,
        "description": description,
    })
    save_transactions(transactions)
    print("Expense added successfully!")

def view_transactions(transactions):
    print("\n--- All Transactions ---")
    if len(transactions) == 0:
        print("No transactions recorded yet.")
        return

    print(f"{'No.':<5}{'Type':<10}{'Category':<15}{'Amount':>10}   Description")
    print("-" * 65)
    for i in range(len(transactions)):
        t = transactions[i]
        print(f"{i + 1:<5}{t['type']:<10}{t['category']:<15}{t['amount']:>10.2f}   {t['description']}")

def search_by_category(transactions):
    print("\n--- Search by Category ---")
    category = input("Enter category to search: ").strip().lower()
    found = False
    for t in transactions:
        if t["category"].lower() == category:
            print(f"{t['type']} - {t['category']} - {t['amount']:.2f} - {t['description']}")
            found = True
    if not found:
        print(f"No transactions found in category '{category}'.")