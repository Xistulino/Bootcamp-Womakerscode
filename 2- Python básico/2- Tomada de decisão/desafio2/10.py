"""
Faça um programa que lê três números inteiros e os mostra em ordem
crescente.
"""

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 <= n2 <= n3:
    print(n1, n2, n3)
elif n1 <= n3 <= n2:
    print(n1, n3, n2)
elif n2 <= n1 <= n3:
    print(n2, n1, n3)
elif n2 <= n3 <= n1:
    print(n2, n3, n1)
elif n3 <= n1 <= n2:
    print(n3, n1, n2)
else:  
    print(n3, n2, n1)
