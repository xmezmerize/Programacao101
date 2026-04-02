# Dicionários

dados_pessoais = {
    "nome": "João",
    "idade": 25,
    "cidade": "Belo Horizonte"
}

print(dados_pessoais)
print(dados_pessoais["nome"])
print(dados_pessoais.get("idade"))

# atribui um valor a uma nova chave
print(dados_pessoais.get("altura", 1.75)) 

#sobrescrever elementos
dados_pessoais["nome"] = "Vítor"
print(dados_pessoais)

# chave de chaves
dict_ex = {
    "texto": "sla",
    "numero": "13",
    "objeto": {"chave": "valor"},
    "vator": [1,2,3,4,5],
    "tupla": (1,2,3)
}

print(dict_ex)

outro_ex = {
    "endereco": {"rua": "caicaras",
                 "bairro": "caicaras",
                 },
    "outro": "valor2"
}

print(outro_ex)
print(outro_ex["endereco"])

# funcoes
print(dados_pessoais.items())


# atualizando
dict1 = {"nome": "felipe"}
dict2 = {"nome": "pedro"}

dict1.update(dict2)

print(dict1)
