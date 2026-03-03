"""
Certo dia, o Prof. Humberto José Roberto fez o seguinte 
questionamento: se o zero à esquerda de um número não 
tem valor algum, por que teria em outras posições de um 
número? Portanto, ele pede sua ajuda para, ao somar dois 
valores inteiros, que o resultado seja exibido segundo o 
raciocínio dele, ou seja, sem os zeros. Por exemplo, ao 
somar 15 + 5, o resultado correto seria 20, mas com esta 
nova ideia, o novo resultado seria 2. Ao somar 99 + 6, o 
resultado correto seria 105, mas com esta nova ideia, o 
novo resultado seria 15. Escreva um programa que lê dois 
números inteiros (pode assumir que eles não têm o algarismo 
zero), some os mesmos e, caso o resultado tenha algum algarismo 
zero, então os retire antes de imprimir na tela.

Exemplo de execução do programa:

Digite o primeiro número: 7 
Digite o segundo número: 5 
Resultado: 12

2º Exemplo de execução do programa:

Digite o primeiro número: 99 
Digite o segundo número: 6 
Resultado: 15
"""

# entrada
numero1 = int(input("Digite um número inteiro: "))
numero2 = int(input("Digite um 2º número inteiro: "))

# processamento
num1_replace = str(numero1).replace("0", "")
num2_replace = str(numero2).replace("0", "")

str_to_num1 = int(num1_replace)
str_to_num2 = int(num2_replace)

soma = str_to_num1 + str_to_num2

print(f"Resultado: {soma}")
