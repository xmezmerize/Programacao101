"""
Chandler e Mônica vão ao cinema no domingo à noite. Para deixar o encontro 
mais animado, eles decidem fazer um jogo de perguntas e respostas para escolher 
qual filme irão assistir. Os seguintes filmes estão cartaz: Frozen, Shrek, 
Todo Mundo em Pânico, Halloween, Diário de uma Paixão, Como se Fosse a Primeira Vez. 
E eles se categorizam como na figura (film_diagram):

Elabore um programa que faça as perguntas como no diagrama, recebendo como entrada 1 
(representando a resposta SIM) e 0 (representando a resposta NÃO) e então imprima o 
filme escolhido. Apenas faça as perguntas que sigam o fluxo do diagrama. Dica: você 
precisará criar inputs para as perguntas que surgirem ao longo do jogo, ou seja, não 
serão todos os inputs no início do programa.
"""

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
