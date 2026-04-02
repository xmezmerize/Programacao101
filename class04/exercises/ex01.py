# 1. Contagem de palavras repetidas

frase = str(input("Digite sua frase: "))
palavras = frase.replace(",", "").lower().split()

resultado = {}

for palavra in palavras:
    if palavra in resultado:
        resultado[palavra] += 1
    else:
        resultado[palavra] = 1
print(resultado)
