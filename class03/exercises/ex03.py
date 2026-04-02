# 3

# entrada
frase = input("Digite aqui sua mensagem: ").upper()

vogais = "AEIOU"
contagem = {}

for letra in frase.upper():
    if letra in vogais:
        contagem[letra] = contagem.get(letra, 0) + 1

print(contagem)
