import random
words = ["jungle" , "piano" , "pencil" , "computer" , "spain" , "forest" , "atheist"]
word = random.choice(words)

print(" ")
print("This is the hangman game, a game where you need to guess a random word given the letters you say")
print("To give your final answer, type 'Answer'")
letter_count = sum(char.isalpha() for char in word)
print("Your word has" , letter_count , "letters")

while True:
    print(" ")
    try1 = input("Insert the letter you think that is on the word or try to hit the answer: ").lower()
    
    if try1 in word:
        positions = [i + 1 for i, letter in enumerate(word.lower()) if letter == try1]
        print("The letter" , try1 , " is the position number ", positions)
    elif try1.lower() == "answer":
        print(" ")
        answer = input("What word do you think that is the hidden word?: ")
        if answer == word:
            print("Congratulations, you hit the answer")
            break
        else:
            print("Wrong answer, you lost the game")
            break
    else:
        print(" ")
        print("The letter you inserted is not in the word")