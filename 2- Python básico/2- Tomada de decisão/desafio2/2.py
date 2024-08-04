"""
Faça um Programa que pergunte em que turno você estuda. Peça para
digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom
Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""

print('Digite o turno em que você estuda.')
print('Possíveis Turnos Escolares: M: Matutino, V: Vespertino e N: Noturno')

nome = str(input('Digite seu nome: '))
turno = str(input('Em que turno você estuda?: ')).upper()

if turno == 'M':
    print(f'Bom Dia,{nome}!')
elif turno == 'V':
    print(f'Boa Tarde, {nome}!')
elif turno == 'N':
    print(f'Boa Noite, {nome}!')
else:
    print('Valor invalido!')