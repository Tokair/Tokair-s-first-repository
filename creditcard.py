credit_card = input('Insert your credit card: ')
credit_card2 = credit_card.replace(" " , "").replace("-", "")
credit_card3 = credit_card2[:4]
print(f"The first four characters of your credit card are: {credit_card3}")