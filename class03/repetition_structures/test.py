# para achar números pares
for numero in range(0,11):
    if numero % 2 == 0:
        print(numero)

print("\n")

# para achar múltiplos
for numero in range(0,11):
    if numero % 3 == 0:
        print(numero)

print("\n")

# usando conversões para delimitadores
s = ""
limite = int(input("> "))
for numero in range(0, limite+1):
    if numero % 2 == 0:
        ultimo_elemento_par = (limite if limite%2==0 else limite-1) # validação - programa para no ultimo elemento par
        delimitador = ", " if numero < limite else "" # delimitador de virgulas
        s = s + str(numero) + delimitador # juntando a contagem do vetor ao delimitador

print(s)
