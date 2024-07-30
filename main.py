# Simple Calculator

def add(): # Function for sum
    num1 = int(input("\nEnter the 1st number to add: "))
    num2 = int(input("Enter the 2nd number to add: "))
    sum = num1 + num2
    print(f"\n{num1} + {num2} = {sum}")

def sub(): # Function for subtraction
    num1 = int(input("\nEnter the 1st number to subtract: "))
    num2 = int(input("Enter the 2nd number to subtract: "))
    difference = num1 - num2
    print(f"\n{num1} - {num2} = {difference}")

def multi(): # Function to mutiply
    num1 = int(input("\nEnter the 1st number to multiply: "))
    num2 = int(input("Enter the 2nd number to multiply: "))
    product = num1 * num2
    print(f"\n{num1} x {num2} = {product}")

def div(): # Function to divide
    num1 = int(input("\nEnter the 1st number to divide: "))
    num2 = int(input("Enter the 2nd number to divide: "))
    quotient = num1 / num2
    print(f"\n{num1} ÷ {num2} = {quotient}")

while True:
    # Creating Program's Main Menu
    print("\n*** Simple Calculator ***")
    choice = int(input("\nPress 1 - Sum\nPress 2 - Subtraction\nPress 3 - Multiplication\nPress 4 - Division\nPress 5 - Quit/Exit\n\nSelect an option: "))

    # Creating Condition

    if choice<1 or choice>5:
        print("\nInvalid choice, Select number between 1 and 5")
    elif choice == 1:
        add()
    elif choice == 2:
        sub()
    elif choice == 3:
        multi()
    elif choice == 4:
        div()
    elif choice == 5:
        break