print("Programa para calcular o determinante de uma matriz 2x2")
print()

# Entrada de dados
print()

matriz = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        matriz[i][j] = float(input(f"Informe o valor da linha {i + 1}, coluna {j + 1}: "))

print()

# Processamento
determinante = matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]

# Saída de dados
print(f"Determinante = {determinante:.2f}")

print()