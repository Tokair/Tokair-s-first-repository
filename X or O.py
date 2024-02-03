o_counter = 0
x_counter = 0
XO = input('Insert a string with the letters "X" or "O": ')
for x in XO.lower():
    XO.lower()
    if x == "x":
        x_counter +=1
    elif x == "o":
        o_counter += 1
if o_counter == x_counter:
    print("The amount of Xs is equal to the amount of Os")
else:
    print("The amount of Xs is not equal to the amount of Os")