"""
Implemente um programa que classifique um aluno com base em sua
pontuação em um exame. O programa deverá solicitar uma nota de 0 a 10. Se
a pontuação for maior ou igual a 7, o aluno é aprovado; caso contrário, é
reprovado.
"""
nota = int(input('Digite a nota do aluno (entre 0 e 10): '))

while nota < 0 or nota > 10:
    print('Valor inválido. Tente novamente.')
    nota = int(input('Digite a nota do aluno (entre 0 e 10): '))

if nota >= 7:
    print('Aluno Aprovado!')
else:
    print('Aluno Reprovado!')
