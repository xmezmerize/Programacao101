# 2

# entrada
numero1 = int(input("Digite um número inteiro: "))
numero2 = int(input("Digite um 2º número inteiro: "))

# processamento
num1_replace = str(numero1).replace("0", "")
num2_replace = str(numero2).replace("0", "")

str_to_num1 = int(num1_replace)
str_to_num2 = int(num2_replace)

soma = str_to_num1 + str_to_num2

print(f"Resultado: {soma}")
