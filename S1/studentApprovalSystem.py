assiduidade = float(input("Digite a assiduidade (%): "))
nota = float(input("Digite a nota (0 a 20): "))

if assiduidade < 75:
situacao = "Reprovado"
else:
if nota <= 5:
situacao = "Reprovado"
elif nota < 10:
situacao = "Exame"
else:
situacao = "Aprovado"

print("Situação do aluno:", situacao)
