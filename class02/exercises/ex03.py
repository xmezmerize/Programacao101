# 3

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
