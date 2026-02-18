inferior = int(input("Digite o limite inferior: "))
superior = int(input("Digite o limite superior: "))

soma = 0

print("Números pares no intervalo aberto:")

for i in range(inferior + 1, superior):
if i % 2 == 0:
print(i)
soma += i

print("Soma dos números pares:", soma)
