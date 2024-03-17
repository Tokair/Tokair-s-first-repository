#objetivo do código: ver os items em comum digitados em ambas as listas pelo usuário e mostrar esses intenss
a = []
b = []
while True:
    ask_a = input("Digite um número para inserir na primeira lista, para terminar digite 'Terminar': ")
    if ask_a.lower() == "terminar":
        print("")
        break
    elif ask_a.isdigit():
        a.append(ask_a)
    elif ask_a.isdigit == '0':
        a.append(ask_a)
    else:
        print("Por favor insira somente números válidos")
while True:
    ask_b = input("Digite um número para inserir na SEGUNDA lista, para terminar digite 'Terminar': ")
    if ask_b.lower() == "terminar":
        print("")
        break
    elif int(ask_b):
        b.append(ask_b)
    elif ask_b == '0':
        b.append(ask_b)
    else:
        print("Por favor insira somente números válidos")

commonitems = set(a) & set(b)
            
if commonitems:            
    print("Items em comum em ambas as listas: ", commonitems)
else:
    print("não há intens em comum nas listas")