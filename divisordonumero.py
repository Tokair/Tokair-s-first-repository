dividendo = int(input("Insira um número (de preferência par): "))
divisores = []
for i in range(1 , dividendo + 1):
    if dividendo % i == 0:
        divisores.append(i)
print(f"Os divisores de {dividendo} são: {divisores}")