total = int(input("Digite o total de eleitores: "))

brancos = int(input("Digite o número de votos brancos: "))
nulos = int(input("Digite o número de votos nulos: "))
validos = int(input("Digite o número de votos válidos: "))

porc_brancos = (brancos / total) * 100
porc_nulos = (nulos / total) * 100
porc_validos = (validos / total) * 100

print("Porcentagem de votos brancos: {:.2f}%".format(porc_brancos))
print("Porcentagem de votos nulos: {:.2f}%".format(porc_nulos))
print("Porcentagem de votos válidos: {:.2f}%".format(porc_validos))
