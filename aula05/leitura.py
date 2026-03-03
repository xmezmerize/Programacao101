# Leitura de arquivos

arquivo = open("exemplo.txt", "r")
conteudo = arquivo.read()
arquivo.close()
print(conteudo)

"""
um pouco mais seguro e não preciso de .close() pois tudo está em 
arquivo e quando nãu uso ja fecha

readlines() -> lê linha a linha
"""
with open("exemplo.txt", "r") as arquivo:
    conteudo = arquivo.readlines()
    print(conteudo)
    
"""
r - leitura (read)
w - escrita (write)
a - anexar (adiciona ao final do arquivo)
b - binario (combina com 'r', 'w' ou 'a')
x - criacao (gera um erro se o arquivo ja existe)
"""
