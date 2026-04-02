# 2

# entrada
numero1 = float(input("Quanto você recebe por hora trabalhada? "))
numero2 = float(input("Qual o número de horas trabalhadas por dia? "))
mes = 30

# processamento
ganho_por_dia = numero1 * numero2
salario_mensal = ganho_por_dia * mes

# saída
print(f"Seu salário é de: R${salario_mensal}")
