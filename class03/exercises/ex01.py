# 1

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
