"""
Salário

Vamos receber (input) dos números do usuário e guardar nas 
variáveis "numero1" e "numero2". A 1º será o valor que o
empregado recebe por hora trabalhada e o 2º o número de 
horas. Calcule o valor total e coloque na variável 
"salario", considerando que o mês tem 30 dias.
"""

# entrada
numero1 = float(input("Quanto você recebe por hora trabalhada? "))
numero2 = float(input("Qual o número de horas trabalhadas por dia? "))
mes = 30

# processamento
ganho_por_dia = numero1 * numero2
salario_mensal = ganho_por_dia * mes

# saída
print(f"Seu salário é de: R${salario_mensal}")
