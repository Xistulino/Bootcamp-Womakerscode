"""
Peça ao usuário para informar o ano de nascimento. Em seguida,
calcule e imprima a idade atual.
"""

ano_atual = int(input('Digite o ano atual: '))
ano_nascimento = int(input('Digite seu ano de nascimento: '))

calculo = ano_atual - ano_nascimento

print(f'Você tem {calculo} de idade')