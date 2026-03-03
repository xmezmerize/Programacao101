# 3 - Sistema de cadastro de alunos e notas

alunos = {}

while True:
    opcao = input("Deseja adicionar um aluno? (S/N): ").upper()
    
    if opcao == "N":
        break
    
    nome = input("Digite o nome do aluno: ")
    entrada = input(f"Digite as notas de {nome}: ")
    entrada = entrada.replace(",", " ")
    notas = list(map(float, entrada.split()))
    
    alunos[nome] = notas

print("\nMédias dos alunos:")

maior_media = 0
melhor_aluno = ""

for nome, notas in alunos.items():
    media = sum(notas) / len(notas)
    print(f"{nome}: {media:.2f}")
    
    if media > maior_media:
        maior_media = media
        melhor_aluno = nome

print(f"\nA maior média é de {melhor_aluno}: {maior_media:.2f}")
