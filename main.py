import os
import csv
from datetime import datetime

FILENAME = 'expenses.csv'
CATEGORIES = ['Rent', 'Bills', 'Travel', 'Health', 'Other']

def initialize_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Date', 'Category', 'Description', 'Amount'])

            print(f"Initialized {FILENAME} successfully.")

def add_expense():
    while True:
        print("\nSelect a category:")
        for i, cat in enumerate(CATEGORIES, 1):
            print(f"{i}. {cat}")
        try:
            cat_choice = int(input("Enter your choice: "))
            if 1 <= cat_choice <= len(CATEGORIES):
                category = CATEGORIES[cat_choice - 1]
                break
            else:
                print("Enter a number between 1-5.")
        except ValueError:
            print("Enter a number.")
    
    description = input("Enter a description: ")

    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount < 0:
                print("Amount cannot be negative.")
            else:
                break
        except ValueError:
            print("Enter a number.")
    
    date = datetime.now().strftime("%d-%m-%Y")

    with open(FILENAME, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([date, category, description, f"{amount:.2f}"])

        print("Expense added successfully.")


def main():
    initialize_file()
    while True:
        print("\n--- Expenses Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Expenses Summary")
        print("4. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                add_expense()
            elif choice == '2':
                pass
            elif choice == '3':
                pass
            elif choice == '4':
                print("Exiting program...")
                break
            else:
                print("Enter a number between 1-4.")
        except ValueError:
            print("Enter a number.")

main()
        
    