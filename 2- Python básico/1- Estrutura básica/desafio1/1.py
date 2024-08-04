"""Faça um Programa que peça dois números, realize as principais
operações soma, subtração, multiplicação, divisão"""

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1*n2
divisao = n1 / n2

print(f'O resultado dos valores são soma: {soma}, subtração: {subtracao}, multiplicação: {multiplicacao} e divisão: {divisao:.0f}')
