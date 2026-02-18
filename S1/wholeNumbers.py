maior = None
menor = None

for i in range(10):
numero = int(input(f"Digite o {i+1}º número: "))

if i == 0:
maior = numero
menor = numero
else:
        
if numero > maior:
maior = numero
if numero < menor:
menor = numero

print("Maior número:", maior)
print("Menor número:", menor)
