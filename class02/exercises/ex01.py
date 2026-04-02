# 1

# entradas
valor_da_hora_trabalhada = float(input("Digite o valor da sua hora de serviço: "))
dias_trabalhados = int(input("Digite quantos dias trabalhou durante o mês: "))
horas_trabalhadas_por_dia = int(input("Digite quantas horas trabalha por dia: \n"))

# processamento
quantidade_de_horas_por_mes = dias_trabalhados * horas_trabalhadas_por_dia
salario_mensal = valor_da_hora_trabalhada * quantidade_de_horas_por_mes

imposto_renda = 0

if salario_mensal <= 900.00:
    imposto_renda = 0.0
elif salario_mensal > 900.00 and salario_mensal <= 1500.00:
    imposto_renda = salario_mensal * 0.05
elif salario_mensal > 1500.00 and salario_mensal <= 2500.00:
    imposto_renda = salario_mensal * 0.1
else:
    imposto_renda = salario_mensal * 0.2

inss = salario_mensal * 0.1
fgts = salario_mensal * 0.11
total_descontos = inss + fgts + imposto_renda

# saídas
print(f"Seu salário mensal bruto é de: R${salario_mensal:.2f}\n")
print(f"O valor do seu IR é de: R${imposto_renda:.2f}\n")
print(f"Valor do INSS: R${inss:.2f}\n")
print(f"Valor do FGTS: R${fgts:.2f}\n")
print(f"O valor total de imposto pagos esse mês é de: R${total_descontos:.2f}")
