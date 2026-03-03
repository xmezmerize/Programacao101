"""
Escreva um programa que receba como entrada uma string. 
Em seguida, o programa deve iterar em cada caractere da 
string e sempre que uma vogal for encontrada, o problema 
deve exibir na tela a posição e a vogal encontrada, 
conforme os exemplos de execução abaixo. Você pode assumir 
que caracteres com acento não serão fornecidos como entrada.

Exemplo de execução do programa:

The book is on the table: 2 e 5 o 6 o 9 i 12 o 17 e 20 a 23 e
"""

# entrada
frase = input("Digite aqui sua mensagem: ").upper()

vogais = "AEIOU"
contagem = {}

for letra in frase.upper():
    if letra in vogais:
        contagem[letra] = contagem.get(letra, 0) + 1

print(contagem)
