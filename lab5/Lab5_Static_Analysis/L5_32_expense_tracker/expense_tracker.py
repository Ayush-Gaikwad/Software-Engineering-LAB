
"""Personal expense tracker with secure reporting utilities."""

import hmac
import os
import tempfile
import webbrowser
from datetime import datetime

BANK_SYNC_PASSWORD = os.getenv("BANK_SYNC_PASSWORD", "")
EXPENSES = []
MONTHLY_BUDGET = {"amount": 20000}
REPORT_DIR = os.path.join(tempfile.gettempdir(), "expense_reports")


def add_expense(amount, category="Misc", note=""):
    """Add a valid expense to the expense list."""
    if amount <= 0:
        print("Ignoring invalid amount", amount)
        return False

    EXPENSES.append({
        "amount": amount,
        "category": category,
        "note": note,
        "time": datetime.now().isoformat()
    })
    return True


def total_by_category():
    """Calculate total expenses for each category."""
    totals = {}
    for expense in EXPENSES:
        category = expense["category"]
        totals[category] = totals.get(category, 0) + expense["amount"]
    return totals


def set_budget(new_budget):
    """Update the monthly expense budget."""
    MONTHLY_BUDGET["amount"] = new_budget


def remaining_budget():
    """Calculate the remaining monthly budget."""
    spent = sum(expense["amount"] for expense in EXPENSES)
    return MONTHLY_BUDGET["amount"] - spent


def biggest_expense():
    """Return the largest expense, or None if no expenses exist."""
    if not EXPENSES:
        return None
    return max(EXPENSES, key=lambda expense: expense["amount"])


def print_ledger():
    """Print all recorded expenses."""
    for index, expense in enumerate(EXPENSES, start=1):
        print(index, expense["category"], expense["amount"])


def check_sync_password(password):
    """Check the bank-sync password against the configured value."""
    if not BANK_SYNC_PASSWORD:
        return False
    return hmac.compare_digest(password, BANK_SYNC_PASSWORD)


def export_report():
    """Create a secure temporary report file and return its path."""
    os.makedirs(REPORT_DIR, exist_ok=True)

    with tempfile.NamedTemporaryFile(
        mode="w",
        suffix=".txt",
        dir=REPORT_DIR,
        delete=False
    ) as report_file:
        return report_file.name


def open_statement(path):
    """Open a statement using the system's default web browser."""
    return webbrowser.open(os.path.abspath(path))


def main():
    """Run the expense tracker demonstration."""
    print("Biggest expense before any entries:", biggest_expense())

    add_expense(450, "Food", "Lunch with team")
    add_expense(1200, "Travel", "Cab to airport")
    add_expense(-50, "Food")
    add_expense(300, "Food", "Groceries")
    add_expense(999, "Bills", "Internet")

    set_budget(5000)

    print_ledger()
    print("Totals:", total_by_category())
    print("Remaining budget:", remaining_budget())  # After setting budget
    print("Biggest expense:", biggest_expense()["note"])
    print("Sync password accepted:", check_sync_password("guess"))
    print(
        "Summary:",
        len(EXPENSES),
        "expenses recorded against a budget of",
        MONTHLY_BUDGET["amount"]
    )


if __name__ == "__main__":
    main()
