import csv
from datetime import datetime

FILE_NAME = "expense_tracker/expenses.csv"

# --------------------------
# 1. Initialize the file
# --------------------------
def initialize_file():
    try:
        with open(FILE_NAME, mode='x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Amount", "Category", "Note"])
    except FileExistsError:
        pass  # file already exists


# --------------------------
# 2. Add a new expense
# --------------------------
def add_expense():
    try:
        amount = float(input("Enter amount spent: "))
        category = input("Enter category (e.g. food, transport): ")
        note = input("Optional note (press enter to skip): ")
        date = datetime.now().strftime("%Y-%m-%d")

        with open(FILE_NAME, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date, amount, category, note])
        
        print("✅ Expense added!\n")
    except ValueError:
        print("❌ Invalid input. Please enter a valid number.")


# --------------------------
# 3. View all expenses
# --------------------------
def view_all_expenses():
    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            print("\n📋 All Expenses:\n")
            for row in reader:
                print(f"{row[0]} | Rs.{row[1]} | {row[2]} | {row[3]}")
            print()
    except FileNotFoundError:
        print("❌ No expenses found. Start by adding one.")


# --------------------------
# 4. View total spent
# --------------------------
def view_total():
    total = 0
    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                total += float(row["Amount"])
        print(f"\n💰 Total spent: Rs.{total:.2f}\n")
    except FileNotFoundError:
        print("❌ No data to calculate total.")


# --------------------------
# 5. View by category
# --------------------------
def view_by_category():
    category = input("Enter category to search: ").lower()
    found = False
    print(f"\n🔍 Expenses in category: {category}\n")
    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["Category"].lower() == category:
                    print(f"{row['Date']} | Rs.{row['Amount']} | {row['Note']}")
                    found = True
        if not found:
            print("⚠️ No expenses in this category.")
    except FileNotFoundError:
        print("❌ No data available.")


# --------------------------
# 6. Menu
# --------------------------
def menu():
    while True:
        print("===== Daily Expense Tracker =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Expenses by Category")
        print("4. View Total Spent")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_all_expenses()
        elif choice == "3":
            view_by_category()
        elif choice == "4":
            view_total()
        elif choice == "5":
            print("👋 Goodbye! Stay on budget.")
            break
        else:
            print("❌ Invalid choice. Try again.\n")


# --------------------------
# Main Entry
# --------------------------
if __name__ == "__main__":
    initialize_file()
    menu()
