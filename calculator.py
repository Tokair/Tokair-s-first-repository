import math
def add():
    print()
    num1 = float(input("Insert the first number: "))
    num2 = float(input("Insert the second number: "))
    result = num1 + num2
    print("The result is: ", result)

def subtraction():
    print()
    num1 = float(input("Insert the first number: "))
    num2 = float(input("Insert the second number: "))
    result = num1 - num2
    print("Your result is: ", result)

def multiplication():
    print()
    num1 = float(input("Insert the first number: "))
    num2 = float(input("Insert the second number: "))
    result = num1 * num2
    print("Your result is: ", result)

def division():
    print()
    num1 = float(input("Insert the first number: "))
    num2 = float(input("Insert the second number: ")) 
    if num2 == 0:
        print("cannot divide by zero")
    else:
        result = num1 / num2
        print("Your result is: ", result)

def raditiation():
    print()
    num1 = float(input("Insert the first number: "))
    num2 = float(input("Insert the second number: "))
    result = num1 ** num2
    print("Your result is:", result)

def square_root():
    print()
    num = float(input("what number would you like to have the square root? "))
    if num < 0:
        print("It is not possible to calculate the square root of a negative number")
    else:
        result = math.sqrt(num)
        print("Your result is: ", result)
        
while True:
    print()
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Raditiation")
    print("6.Square root")
    print("7.Leave")
    choice = input("Type the number of your choice:")
    if choice == "1":
        add()
    elif choice == "2":
        subtraction()
    elif choice == "3":
        multiplication()
    elif choice == "4":
         division()
    elif choice == "5":
        raditiation()
    elif choice == "6":
        square_root()
    elif choice == "7":
        print("Leaving calculator, goodbye!")
        break
else:
    print("Invalid choice, type a number between 1-7")