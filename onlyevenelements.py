#this code's goal is to show a list with only even numbers typed by the user.
evenlist = []
while True:
    even = input('Insira um número, para terminar digite "terminar" : ')
    if even == "terminar":
        print("Todos os números pares dentre os números digitados: " , evenlist)
        break
    elif int(even) % 2 == 0:
        evenlist.append(even)