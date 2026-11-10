print("Programa para somar duas matrizes 4x3")
print()

# Entrada de dados
print()

matriz1 = [[0] * 3 for i in range(4)]
matriz2 = [[0] * 3 for i in range(4)]
soma = [[0] * 3 for i in range(4)]

print("Primeira matriz")
for i in range(4):
    for j in range(3):
        matriz1[i][j] = float(input(f"Informe o valor da linha {i + 1}, coluna {j + 1}: "))

print()

print("Segunda matriz")
for i in range(4):
    for j in range(3):
        matriz2[i][j] = float(input(f"Informe o valor da linha {i + 1}, coluna {j + 1}: "))

print()

# Processamento
for i in range(4):
    for j in range(3):
        soma[i][j] = matriz1[i][j] + matriz2[i][j]

# Saída de dados
print("Matriz soma")
for i in range(4):
    for j in range(3):
        print(f"{soma[i][j]:8.2f}", end="")
    print()

print()