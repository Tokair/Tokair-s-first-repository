def Reversestring():
    x = input("Digite uma frase ou sequência de palavras: ")
    y = x.split()
    y.reverse()
    print(' '.join(y))
    
Reversestring()