"""
Calculadora

Escreva um código que receba (input) de dois números do usuário
e guarde na variáveis "numero1" e "numero2". Em seguida, calcule 
a soma desses valores e guarde na variavel "soma". Depois imprima 
o resultado (print)
"""

# entrada
numero1 = float(input("Digite o 1º valor: "))
numero2 = float(input("Digite o 2º valor: "))

# processamento
soma = numero1 + numero2

# saída
print(f"{soma:.2f}")
