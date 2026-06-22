import csv
from datetime import datetime

def add_expense(desc, amount, category):
    with open("expenses.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([desc, amount, category, datetime.now().strftime("%Y-%m-%d")])

def view_expenses():
    with open("expenses.csv", "r") as f:
        for row in csv.reader(f):
            print(row)

def search_category(category):
    with open("expenses.csv", "r") as f:
        for row in csv.reader(f):
            if row[2] == category:
                print(row)

def monthly_total(month):
    total = 0
    with open("expenses.csv", "r") as f:
        for row in csv.reader(f):
            if row[3].startswith(month):
                total += int(row[1])
    print("Monthly Total:", total)

add_expense("Lunch", 200, "Food")
add_expense("Bus Ticket", 50, "Travel")
view_expenses()
search_category("Food")
monthly_total("2026-06")
