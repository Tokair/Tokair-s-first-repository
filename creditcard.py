credit_card = (input("Insert a credit card number: "))
credit_card2 = credit_card.replace(" " , "").replace("-" , "")
first_digit = credit_card2[:4]
print(f"Your credit card's first four characters are: {first_digit}")