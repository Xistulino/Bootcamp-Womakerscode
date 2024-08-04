"""
Faça um Programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês.Calcule e mostre o total do seu
salário no referido mês.
"""

salario_hora = float(input('Digite quanto você ganha por hora:  '))
horas_trabalhadas = float(input('Digite a quantidade de horas trabalhadas:  '))


salario_total = salario_hora * horas_trabalhadas

print(f'Seu salário hora é: R${salario_hora}')
print(f'A quantidade de horas trabalhadas foi:  R${horas_trabalhadas}')
print(f'O salário total será de: R${salario_total}')