"""
Crie um programa que solicite ao usuário três valores inteiros positivos, 
representando os lados de um triângulo. Verifique se os valores formam um 
triângulo válido (a soma de dois lados deve ser sempre maior que o terceiro). 
Se os valores formarem um triângulo, classifique-o em:

Equilátero: todos os lados são iguais.
Isósceles: dois lados são iguais e um diferente.
Escaleno: todos os lados são diferentes.
Se não formarem um triângulo, exiba a mensagem: "Os valores não formam um 
triângulo válido."
"""

# entrada
lado1 = float(input("Digite o valor do 1º lado do seu triângulo: "))
lado2 = float(input("Digite o valor do 2º lado do seu triângulo: "))
lado3 = float(input("Digite o valor do 3º lado do seu triângulo: "))

# processamento/saída
if lado1 == lado2 == lado3:
    print(f"Seu triângulo é EQUILÁTERO de lados igual a {lado1}.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    if lado1 + lado2 > lado3 or lado1 + lado3 > lado2 or lado1 + lado3 > lado2:
        print("Não é possível formar um triângulo!")
    else:
        print("Seu triângulo é ISÓSCELES.")    
else:
    if lado1 + lado2 > lado3 or lado1 + lado3 > lado2 or lado1 + lado3 > lado2:
        print("Não é possível formar um triângulo!")
    else:
        print("Seu triângulo é ESCALENO")
