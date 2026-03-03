"""
Em outubro chove muito na cidade de Forks. Escreva um programa 
que seja capaz de ler do teclado os 7 valores correspondentes 
ao índice pluviométrico de cada dia da semana. O programa deve 
então determinar e imprimir o índice pluviométrico médio, o 
índice pluviométrico mínimo e o dia de ocorrência do mínimo. 
Caso o valor mínimo apareça em mais de um dia, deve-se considerar 
o primeiro dia em que ele apareceu. Não é necessário checar a 
validade dos dados, pois só serão inseridos dados válidos.

Exemplo de execução do programa:

Qual o Índice Pluviométrico do dia 1? 80.0 
Qual o Índice Pluviométrico do dia 2? 80.0 
Qual o Índice Pluviométrico do dia 3? 10.0 
Qual o Índice Pluviométrico do dia 4? 10.0 
Qual o Índice Pluviométrico do dia 5? 40.0 
Qual o Índice Pluviométrico do dia 6? 40.0 
Qual o Índice Pluviométrico do dia 7? 50.0

Índice Médio: 44.29 
Índice Mínimo: 10.00 
Dia do Mínimo: 3

2º Exemplo de execução do programa:

Qual o Índice Pluviométrico do dia 1? 44.0 
Qual o Índice Pluviométrico do dia 2? 43.58 
Qual o Índice Pluviométrico do dia 3? 21.22 
Qual o Índice Pluviométrico do dia 4? 34.7 
Qual o Índice Pluviométrico do dia 5? 90.2 
Qual o Índice Pluviométrico do dia 6? 11.0 
Qual o Índice Pluviométrico do dia 7? 20.07

Índice Médio: 37.82 
Índice Máximo: 11.00 
Dia do Mínimo: 6
"""

# entrada
segunda = float(input("Qual o índice pluviométrico da segunda-feira: "))
terca = float(input("Qual o índice pluviométrico da terça-feira: "))
quarta = float(input("Qual o índice pluviométrico da quarta-feira: "))
quinta = float(input("Qual o índice pluviométrico da quinta-feira: "))
sexta = float(input("Qual o índice pluviométrico da sexta-feira: "))
sabado = float(input("Qual o índice pluviométrico do sábado: "))
domingo = float(input("Qual o índice pluviométrico do domingo: "))

# processamento
indice_pluviometrico_medio = (segunda + terca + quarta + quinta + sexta + sabado + domingo) / 7

indice = {
    "segunda": segunda,
    "terça": terca,
    "quarta": quarta,
    "quinta": quinta,
    "sexta": sexta,
    "sabado": sabado,
    "domingo": domingo
}

menor_indice = min(indice.values())
dia_do_menor_indice = min(indice, key=indice.get)

maior_indice = max(indice.values())
dia_do_maior_indice = max(indice, key=indice.get)

# saída
print("\n")
print(f"Índice médio: {indice_pluviometrico_medio:.2f}")
print(f"O dia de menor índice pluviométrico foi {dia_do_menor_indice} com {menor_indice:.2f}.")
print(f"O dia de maior índice pluviométrico foi {dia_do_maior_indice} com {maior_indice:.2f}.")
