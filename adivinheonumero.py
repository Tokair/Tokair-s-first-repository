import random

while True:
    x = random.randint(1, 9)
    print("""Adivinhe o número secreto, um jogo por Miguel Lobo
    
    O número secreto é um número entre 1 - 9, tente adivinhá-lo. 
    
    Para sair, digite "Sair" 
    
     """)
    
    while True:
        try:
            print('')
            choice = input("Adivinhe o número: ")
            if choice.lower() == "sair":
                break
            elif int(choice) == x:
                print("Você acertou")
                break
            elif int(choice) < x:
                print("O número digitado é menor que x")
            elif int(choice) > x:
                print("O número digitado é maior que x")
        except:
            print("")
            print("Insira um número válido")
    question = input("Você deseja jogar novamente?:  ")
    if question.lower() != "sim":
        break
    else:
        print("Obrigado por jogar")