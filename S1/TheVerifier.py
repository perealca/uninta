nome1 = input("Digite o nome da primeira pessoa: ")
altura1 = float(input("Digite a altura da primeira pessoa (em metros): "))
peso1 = float(input("Digite o peso da primeira pessoa (em kg): "))

nome2 = input("Digite o nome da segunda pessoa: ")
altura2 = float(input("Digite a altura da segunda pessoa (em metros): "))
peso2 = float(input("Digite o peso da segunda pessoa (em kg): "))

if peso1 > peso2:
mais_pesada = nome1
elif peso2 > peso1:
mais_pesada = nome2
else:
mais_pesada = "As duas têm o mesmo peso"


if altura1 > altura2:
mais_alta = nome1
elif altura2 > altura1:
mais_alta = nome2
else:
mais_alta = "As duas têm a mesma altura"

print("Pessoa mais pesada:", mais_pesada)
print("Pessoa mais alta:", mais_alta)
