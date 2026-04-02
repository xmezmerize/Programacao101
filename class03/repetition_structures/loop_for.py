# Loop for (para cada) -> esse loop serve quando precisamos passar por todos os elementos de um conjunto ou coleção.

# range
for num in range(5,10, 2): # de 5 até 10 pulando de 2 em 2
    print(num)

print("\n")

# continue
for numero in [1,2,3,4,5]:
    print('ola')
    if numero == 3:
        continue
    print(numero)

print("\n")

# break
for numero in [1,2,3,4,5]:
    print('ola')
    if numero == 3:
        break
    print(numero)

print("\n")

vetor1 = ["Oi", "Como", "Vai?"]

for elemento in vetor1:
    print(elemento)
