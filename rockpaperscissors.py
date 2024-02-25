while True:
    name1 = input("Insert the first player's name: ")
    name2 = input("Insert the second player's name: ")
    print(" ")
    choice1 = int(input(f"""{name1}, your turn, choose between:
    1: Rock
    2: Paper
    3: Scissors(type the number of your choice): """))
    print(" ")
    choice2 = int(input(f"""{name2} , your turn, choose bewteen:
    1: Rock
    2: Paper
    3: Scissors(type the number of your choice): """))
    print(" ")
    
    if choice1 == choice2:
        print("It's a draw, both inserted the same choice")
    elif choice1 == 1 and choice2 == 2:
        print(f"{name2} wins, rock wins against paper")
    elif choice1 == 2 and choice2 ==1:
        print(f"{name1}, wins, paper wins against rock")
    elif choice1 == 2 and choice2 == 3:
        print(f"{name2} wins, scissors win against paper")
    elif choice1 == 3 and choice2 == 2:
        print(f"{name1} wins, scissors win against paper")
    elif choice1 == 3 and choice2 == 1:
        print(f"{name2} wins, rock wins against scissors")
    elif choice1 == 1 and choice2 == 3:
        print(f"{name1} wins, rock wins against scissors")
    else:
        print("Invalid choice")
    print("")
    aftermatch = input("Do you want to play again? Yes/No :")
    if aftermatch.lower() == "no":
        break
    elif aftermatch.lower() == "yes":
        continue