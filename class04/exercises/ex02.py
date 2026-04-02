# 2. Soma de matrizes

def soma_matrizes(matriz1, matriz2):
    return [
        [matriz1[i][j] + matriz2[i][j] for j in range(len(matriz1[0]))]
        for i in range(len(matriz1))
    ]

soma = soma_matrizes(
    [[1,2,3],[4,5,6],[7,8,9]],
    [[9,8,7],[6,5,4],[3,2,1]]
)

print(soma)
