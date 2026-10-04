# Expense Tracker - Installment 2
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

# Expense Input 1
item1 = input("First expense? ")
amount1 = float(input("Amount? "))

# Expense Input 2
item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
print()

#Calculations
# Calculate Total
total = amount1 + amount2
# Calculate Average
average = total / 2

# Summary
print("-" * 40)
print("SUMMARY")
print(f"  - {item1}:\t\t${amount1}")
print(f"  - {item2}:\t\t${amount2}")
print(f"{'Total spent:'}\t\t${total}")
print(f"{'Average:'}\t\t${average}")

# Footer
print("-" * 40)
print("Made by: John Michael Martinez  |  Installment 2")
