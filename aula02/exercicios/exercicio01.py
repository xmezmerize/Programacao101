"""
Sálario líquido

Escreva um programa que peça ao usuário o valor da sua hora de trabalho, 
a quantidade de horas trabalhadas no mês e calcula a sua folha de pagamento. 
São descontados do salário o Imposto de Renda, que depende do salário bruto 
(conforme tabela abaixo), e o INSS, que corresponde a 10% do salário bruto. 
O FGTS corresponde a 11% do salário bruto, no entanto o FGTS não é descontado 
do salário, pois é a empresa que deposita. O salário líquido corresponde ao 
salário bruto menos os descontos.

Salário Bruto	               |   Imposto de Renda

Até R$900	                   |   Isento
Maior que R$900 até R$1500     |   Desconto de 5%
Maior que R$1500 até R$2500	   |   Desconto de 10%
Maior que R$2500               |   Desconto de 20%

Observação: as mensagens exibidas para o usuário deverão ser exatamente como 
apresentado abaixo (mensagens exibidas com os comandos input() e print()).

Exemplo de execução do programa:

Digite o valor da hora de trabalho: 16.0
Digite a quantidade de horas trabalhadas no mês: 160

Salário Bruto: R$ 2560.00

IR: R$ 512.00
INSS: R$ 256.00
FGTS: R$ 281.60

Total de descontos: R$ 768.00
"""

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
