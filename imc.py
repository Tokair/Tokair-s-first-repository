print()
print("Este é um calculador de IMC(Índice de Massa Corporal), onde você pode verificar se o seu peso está adequado.")
print("")
print("OBS:Este é apenas um projeto feito por um adolescente e não deve ser levado a sério. Se tiver quaisquer dúvidas sobre o seu peso consulte um especialista")
peso = float(input("Insira o seu peso(em quilos): "))
altura = float(input("Insira a sua altura(em metros): "))
imc = peso // altura**2
if imc <= 18.5:
    print(f"O seu IMC é {imc}. Você está abaixo do peso")
elif imc <= 24.9:
    print(f"O seu IMC é {imc}. Parabéns, você está dentro do peso.")
elif imc <= 29.9:
    print(f"O seu IMC é {imc}. Você está acima do peso.")
elif imc <= 34.9:
    print(f"O seu IMC é {imc}. Você tem grau de obesidade I.")
elif imc <= 39.9:
    print(f"O seu IMC é {imc}. Você tem grau de obesidade II.")
elif imc >= 40:
    print(f"O seu IMC é {imc}. Você tem grau de obesidade III(ta gordin em).")