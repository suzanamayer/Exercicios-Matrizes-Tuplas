print("Programa para calcular o determinante de uma matriz 3x3")
print()

# Entrada de dados
print()

matriz = [[0] * 3 for i in range(3)]

for i in range(3):
    for j in range(3):
        matriz[i][j] = float(input(f"Informe o valor da linha {i + 1}, coluna {j + 1}: "))

print()

# Processamento
determinante = (matriz[0][0] * matriz[1][1] * matriz[2][2]
                + matriz[0][1] * matriz[1][2] * matriz[2][0]
                + matriz[0][2] * matriz[1][0] * matriz[2][1]
                - matriz[0][2] * matriz[1][1] * matriz[2][0]
                - matriz[0][1] * matriz[1][0] * matriz[2][2]
                - matriz[0][0] * matriz[1][2] * matriz[2][1])

# Saída de dados
print(f"Determinante = {determinante:.2f}")

print()