# 2

# entrada
animacao = int(input("É de animação? (1/0): "))

# processamento/saída
if animacao == 1:
    disney = int(input("É da disney? (1/0): "))
    if disney == 1:
        print("Frozen")
    else:
        print("Shrek")
else:
    live_action = int(input("Seu live action é de Terror? (1/0): "))
    if live_action == 1:
        comedia = int(input("É de comédia? (1/0): "))
        if comedia == 1:
            print("Todo mundo em pânico")
        else:
            print("Halloween")
    elif live_action == 0:
        romance = int(input("É um drama? (1/0): "))
        if romance == 1:
            print("Diário de uma paixão")
        else:
            print("Como se Fosse a Primeira Vez")
