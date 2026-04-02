# entrada
nome = input("Digite seu nome: ")

# processamento
def saudacao(nome):
    return f"Olá {nome}!"

# saída
print(saudacao(nome))
print("\n")


# atribuindo valor "padrão" a um parametro
def saudacao(nome, saudacao="Olá"):
    return saudacao + " " + nome + "!"

print(saudacao("Pedro"))
print("\n")

# soma
def soma(a, b):
    return a + b

print(soma(5, 6))
print("\n")

# função de exibição que usa função anterior para somar
def exibe_resultado(resultado):
    print(f"O resultado da soma é: {resultado}")
    print("\n")

valor1 = float(input("Digite o 1º valor: "))
valor2 = float(input("Digite o 2º valor: "))

resultado = soma(valor1, valor2)
exibe_resultado(resultado)

# função fatorial: permutação -> 5! = 5 * 4 * 3 * 2 * 1 = 120
def fatorial_while(n):
    fatorial = 1
    while n >= 1:
        fatorial *= n  # fatorial = fatorial * n
        n -= 1  # n = n - 1
    return fatorial

def fatorial_for(n):
    fatorial = 1
    for item in range(1, n+1):
        fatorial *= n
        n -= 1
    return fatorial

print("Fatorial com While:", fatorial_while(5))
print("Fatorial com For:", fatorial_for(5))
print("\n")

# Fibonacci
def fib(n):
    """
    Primeiros números da sequência de Fibonacci -> 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 
    377, 610, 987, 1597, 2584, 4181, 6765 ...

    Fórmula Fibonacci: Fn = Fn-1 + Fn-2 -> é uma função recursiva!
    """
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


print(fib(8))
print(fib(15))
print(fib(20))
print("\n")

# Exemplo de cálculo de somatório usando recursão -> 5 + 4 + 3 + 2 + 1 = 15
def somatorio(x):
    if x == 1:
        return 1
    else:
        return x + somatorio(x-1)

numero = int(input("Número para calcular o somatório: "))
print(f"O somatório de {numero} é: {somatorio(numero)}")
