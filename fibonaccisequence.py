while True:
    try:
        fibonnaciseq = [1]
        print()
        choice = int(input("How many fibonnaci sequence numbers do you want?: "))
        def fibonnacicommand():
            last_two = fibonnaciseq[-2:]
            new_number = int(sum(last_two))
            fibonnaciseq.append(new_number)
        
        for x in range(choice - 1):
            fibonnacicommand()
        
        if choice == 1:
            print("Fibonnaci sequence numbers: 1")
        elif choice <= 0:
            print("Please choose a number above 0")
        else:
            print("Fibonnaci sequence: " , fibonnaciseq)
    except ValueError:
        print("Please type ONLY INTEGERS NUMBERS")