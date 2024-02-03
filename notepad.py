notes = []

while True:
    print("\n1- Adicionar notas")
    print("2- Ver notas")
    print("3- Remover notas")
    print("4- Fechar bloco de notas")
    choice = input("\nDigite sua escolha: ")

    if choice == "1":
        new_note = input("\nInsira suas notas: ")
        notes.append(new_note)
        print("\nItem adicionado")
    elif choice == "2":
        for note in notes:
            print("\n",note)
    elif choice == "3":
        remove_number = int(input("\nDigite o número da nota que você gostaria de remover :"))
        notes.pop(remove_number)
        print("\nNota removida")
    elif choice == "4":
        print("\nSaindo do bloco de notas")
        break
    else:
        print("\nEscolha inválida, digite um número entre 1-4")