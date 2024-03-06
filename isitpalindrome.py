print("Palíndromos são textos que lidos de trás para frente são os mesmos. Exemplos: Arara, osso")
print()
string = input("Insira uma palavra: ")
string = string.replace(" ", "")
stringreverse = string[::-1]
if string.lower() == stringreverse.lower():
    print("O texto é um palíndromo")
else:
    print("O texto não é um palíndromo")