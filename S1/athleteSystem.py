idade = int(input("Digite a idade do atleta: "))

if idade >= 5 and idade <= 7:
categoria = "Infantil"
elif idade >= 8 and idade <= 10:
categoria = "Iniciado"
elif idade >= 11 and idade <= 13:
categoria = "Juvenil"
elif idade >= 14 and idade <= 17:
categoria = "Junior"
elif idade >= 18:
categoria = "Sênior"
else:
categoria = "Idade fora das categorias"

print("Categoria:", categoria)
