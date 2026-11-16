print("Programa para separar pessoas por idade")
print()

# Entrada de dados
print()

pessoas = []

for i in range(10):
    nome = input(f"Informe o nome da {i + 1}a pessoa: ")
    idade = int(input(f"Informe a idade da {i + 1}a pessoa: "))
    pessoa = (nome, idade)
    pessoas.append(pessoa)
    print()

# Processamento
# Saída de dados
print("Pessoas com menos de 18 anos")
for i in range(len(pessoas)):
    if pessoas[i][1] < 18:
        print(f"{pessoas[i][0]} - {pessoas[i][1]} anos")

print()
print("Pessoas com 18 anos ou mais")
for i in range(len(pessoas)):
    if pessoas[i][1] >= 18:
        print(f"{pessoas[i][0]} - {pessoas[i][1]} anos")

print()