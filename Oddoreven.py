while True:
    number_input = input("Type a number ")
    if not number_input.isdigit():
        print("Please do not insert strings")
        continue
    
    number_input = int(number_input)
    result = number_input % 2
    if result == 1:
        print("Your number is odd")
    else:
        print("Your number is even")