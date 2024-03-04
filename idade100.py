while True:
    print("")
    birthyear = input("Insira em que ano nasceste: ")
    try:
        birthyear = int(birthyear)
    except ValueError:
        print("")
        print("(Digite um número sem letras)")
        continue
    age100 = birthyear + 100
    print(f"Você irá fazer 100 anos no ano de {age100}")
    break