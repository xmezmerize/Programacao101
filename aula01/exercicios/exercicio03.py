"""
Par ou ímpar

Vamos ler um número inteiro (input) e guardar na variável "num_int".
Verifique se o número é par ou ímpar utilizando o operador de módulo. 
Guarde o resultado na variável paridade, por fim crie a variável 
eh_par para receber a comparação em booleano, se Aparecer True é par, 
se der False ímpar.
"""

# entrada
num_int = int(input("Digite o valor inteiro: "))

# processamento
paridade = num_int % 2
eh_par = paridade == 0

# saída
print(eh_par)
