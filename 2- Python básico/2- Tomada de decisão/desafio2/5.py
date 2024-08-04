"""
Desenvolva um programa que solicite ao usuário os comprimentos dos três
lados de um triângulo e classifique-o como equilátero, isósceles ou escaleno.
equilátero: todos os lados com o mesmo valor
isósceles: dois lados com o mesmo valor
escaleno: todos os lados com medidas distintas.
"""

a = float(input('Digite o primeiro lado do triângulo: '))
b = float(input('Digite o segundo lado do triângulo: '))
c = float(input('Digite o terceiro lado do triângulo: '))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print('O triângulo é Equilátero')
    elif a == b or a == c or b == c:
        print('O triângulo é Isósceles')
    else:
        print('O triângulo é Escaleno')
else:
    print('Não é um triângulo válido')
