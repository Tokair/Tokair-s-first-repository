numero1divisores = []
numero2divisores = []
divisoresemcomum = []

numero1 = int(input("Insira um número (de preferência par): "))
print("")
numero2 = int(input("Insira outro número(de preferência par também): "))
for y in range(1 , numero1 + 1):
    if numero1 % y == 0:
        numero1divisores.append(y)
for z in range(1, numero2 + 1):
    if numero2 % z ==0:
        numero2divisores.append(z)


for i in numero1divisores:
    if i in numero2divisores:
        divisoresemcomum.append(i)
print(f"""Os divisores em comum de {numero1} e {numero2} são: {divisoresemcomum}

O MDC(Máximo Divisor Comum) desses números é: {divisoresemcomum[-1]}""")