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

def show_summary(transactions):
    print("\n--- Summary ---")
    if len(transactions) == 0:
        print("No transactions recorded yet.")
        return

    total_income = 0
    total_expense = 0
    for t in transactions:
        if t["type"] == "Income":
            total_income = total_income + t["amount"]
        else:
            total_expense = total_expense + t["amount"]

    balance = total_income - total_expense

    print("Total Income:", round(total_income, 2))
    print("Total Expenses:", round(total_expense, 2))
    print("Remaining Balance:", round(balance, 2))

def analyze_expenses(transactions):
    print("\n--- Expense Analysis (by Category) ---")
    expenses = [t for t in transactions if t["type"] == "Expense"]

    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return

    df = pd.DataFrame(expenses)
    totals = df.groupby("category")["amount"].sum().round(2)
    totals = totals.sort_values(ascending=False)
    print(totals.to_string())
    print("\nHighest spending category:", totals.idxmax())

def delete_transaction(transactions):
    print("\n--- Delete Transaction ---")
    if len(transactions) == 0:
        print("No transactions to delete.")
        return

    view_transactions(transactions)
    try:
        number = int(input("Enter the number of the transaction to delete: "))
    except ValueError:
        print("Invalid number.")
        return

    if 1 <= number <= len(transactions):
        removed = transactions.pop(number - 1)
        save_transactions(transactions)
        print(f"Deleted: {removed['type']} - {removed['category']} - {removed['amount']:.2f}")
    else:
        print("No transaction with that number.")

def main():
    transactions = load_transactions()

    while True:
        print("\n===== Personal Finance Tracker =====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View All Transactions")
        print("4. Search by Category")
        print("5. Show Summary (Income, Expenses, Balance)")
        print("6. Analyze Expenses by Category")
        print("7. Delete Transaction")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_income(transactions)
        elif choice == "2":
            add_expense(transactions)
        elif choice == "3":
            view_transactions(transactions)
        elif choice == "4":
            search_by_category(transactions)
        elif choice == "5":
            show_summary(transactions)
        elif choice == "6":
            analyze_expenses(transactions)
        elif choice == "7":
            delete_transaction(transactions)
        elif choice == "8":
            print("Goodbye! Your data has been saved.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")


if __name__ == "__main__":
    main()