#o objetivo desse código é pegar todos os números pares digitados pelo usuário, somente os pares
evenlist = []
while True:
    try:
        even = input('Insira um número, para terminar digite "terminar" : ')
        if even == "terminar":
            print("Todos os números pares dentre os números digitados: " , evenlist)
            break
        elif int(even) % 2 == 0:
            evenlist.append(even)
    except:
        print("Digite um número válido")