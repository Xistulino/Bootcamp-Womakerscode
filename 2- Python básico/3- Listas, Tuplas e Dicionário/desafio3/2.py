"""
Faça um Programa que peça as quatro notas de 5 alunos, calcule
e armazene numa lista a média de cada aluno, imprima o número
de alunos com média maior ou igual a 7.0.
"""

# Lista para armazenar as médias dos alunos
medias = []

# Número de alunos
num_alunos = 5

# Loop para cada aluno
for i in range(num_alunos):
    print(f"Aluno {i+1}:")
    notas = []
    
    # Coletar as quatro notas de cada aluno
    for j in range(4):
        while True:
            try:
                nota = float(input(f"Digite a nota {j+1}: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("Nota inválida. Digite uma nota entre 0 e 10.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
    
    # Calcular a média do aluno
    media = sum(notas) / 4
    medias.append(media)

# Contar o número de alunos com média maior ou igual a 7.0
alunos_com_media_maior_igual_7 = sum(1 for media in medias if media >= 7.0)

# Imprimir o resultado
print(f"Número de alunos com média maior ou igual a 7.0: {alunos_com_media_maior_igual_7}")
