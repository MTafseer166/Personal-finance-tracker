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