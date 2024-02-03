import random
while True:
    x = random.randint(-20, -1)
    y = random.randint(1, 20)
    result1 = x - y
    name = input("\nInsert your name: ")
    print("\nGuess the secret number!")
    print("\n By Miguel Lobo")
    print("\nYour secret number, subtracted by ", y , "is ", result1 , " Knowing this, what is the secret number?")
    answer = int(input("Type the secret number: "))
    if x == answer:
        print("Your answer is right! Congratulations, ", name ,)
        print("\nAll credits to Miguel Lobo")
    else:
        print("Your answer is wrong, try again :(")
        print("All credits to Miguel Lobo")
        question = input("Do you wanna try again?")
        
        if question.lower() == "no":
            break