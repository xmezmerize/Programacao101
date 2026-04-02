# Matrizes

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

elemento = matriz[1][2] # linha | coluna

print(elemento)

# diagonal
for i in range(0,3): # [0,1,2]
    elemento = matriz[i][i]
    print(F"{elemento}\n")
    
# diagonal inversa
for i in range(0,3): # [0,1,2]
    elemento = matriz[i][-i]
    print(elemento)
    
# criando matrizes (linha de linhas)
n = int(input("> "))
matriz = []
for i in range(0,n):
    linha = []
    for j in range(0,n):
        linha.append(0)
    matriz.append(linha)
print(matriz)

# criando matriz
matriz = []
for _ in range(0,2):
    linha = []
    for _ in range(0, 2):
        valor = int(input("> "))
        linha.append(valor)
    matriz.append(linha)
print(matriz)
