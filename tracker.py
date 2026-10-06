# Expense Tracker - Installment 3: The Tracker Does Math
# Author: John Michael Martinez
# A personal expense tracker that takes user input and calculates expenses.

# Header
print("=" * 40)

# Title and Tagline
print("\t\tEXPENSE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)

# Main Menu
print("MAIN MENU")
print(" [1] Add an expense\t\t(coming soon)")
print(" [2] View all expenses\t\t(coming soon)")
print(" [3] Show total spent\t\t(coming soon)")
print(" [4] Exit\t\t\t(coming soon)")
print()

# Name
name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")
print()

#Subtotal
subtotal = 0

# Expense Input 1
item1 = input("First expense? ")
amount1 = float(input("Amount? "))
subtotal += amount1

# Expense Input 2
item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal += amount2

# Calculations
average = subtotal / 2

# Tax
tax_percent = int(input("Tax rate %? "))
tax = subtotal * tax_percent / 100
total = subtotal + tax

# Budget
budget = float(input("Your budget? "))
over_budget = total > budget
left = budget - total
print()

# Summary
print("-" * 40)
print("SUMMARY")
print(f"  - {item1}:\t${amount1}")
print(f"  - {item2}:\t${amount2}")
print(f"Subtotal:\t${subtotal}")
print(f"Average:\t${average}")
print(f"Tax ({tax_percent}.0%):\t${tax}")
print(f"Grand total:\t${total}")
print(f"Over budget?\t{over_budget}")
print(f"Left in budget:\t${left}")

# Footer
print("-" * 40)
print("Made by: John Michael Martinez  |  Installment 3")
