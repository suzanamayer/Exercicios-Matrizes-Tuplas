print("Programa para verificar se a matriz 3x3 e identidade")
print()

# Entrada de dados
print()

matriz = [[0] * 3 for i in range(3)]

for i in range(3):
    for j in range(3):
        matriz[i][j] = float(input(f"Informe o valor da linha {i + 1}, coluna {j + 1}: "))

print()

# Processamento
identidade = True

for i in range(3):
    for j in range(3):
        if i == j:
            if matriz[i][j] != 1:
                identidade = False
        else:
            if matriz[i][j] != 0:
                identidade = False

# Saída de dados
if identidade:
    print("A matriz informada é uma matriz identidade")
else:
    print("A matriz informada NÃO é uma matriz identidade")

print()