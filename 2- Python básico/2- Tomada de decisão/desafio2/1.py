"""
Faça um Programa que peça dois números e imprima o maior deles.
"""
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print(f'O maior número digitado é o {n1} ')
elif n1 < n2:
    print(f'O maior número digitado é {n2}')
else:
    print(f'Os dois números digitados são iguais: {n1} e {n2}')