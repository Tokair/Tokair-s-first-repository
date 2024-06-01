import string
import random

word = []

def random_letter():
    return random.choice(string.ascii_letters)

def random_number():
    return str(random.randint(1, 9))

while True:
    try:
        charact = int(input("How many characters do you want in your password? "))
        if charact < 0:
            print("Please type a positive number")
        else:
            break
    except ValueError:
        print("Please type a valid number or use numbers, not letters")

word = []
for x in range(charact):
    if random.randint(0, 1) == 0:
        word.append(random_letter())
    else:
        word.append(random_number())

gword = ' '.join(word)
fword = gword.replace(" ", "")
print("Generated password: " , fword)