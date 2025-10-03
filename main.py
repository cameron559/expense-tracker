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
                pass
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
        
    