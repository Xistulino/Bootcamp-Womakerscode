"""
Criar um programa em Python que solicite três números ao usuário, utilize
estruturas condicionais para determinar o maior entre eles e apresente o
resultado.
"""

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 >= n2 and n1 >= n3:
    print('O primeiro número é o maior!')
elif n2 >= n1 and n2 >= n3:
    print('O segundo número é o maior!')
else:
    print('O terceiro número é o maior!')
