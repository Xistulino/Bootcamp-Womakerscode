"""
Escreva um programa que calcule o salário líquido. Lembrando de
declarar o salário bruto e o percentual de desconto do Imposto de
Renda.
● Renda até R$ 1.903,98: isento de imposto de renda;
● Renda entre R$ 1.903,99 e R$ 2.826,65: alíquota de 7,5%;
● Renda entre R$ 2.826,66 e R$ 3.751,05: alíquota de 15%;
● Renda entre R$ 3.751,06 e R$ 4.664,68: alíquota de 22,5%;
● Renda acima de R$ 4.664,68: alíquota máxima de 27,5%.
"""

salario_bruto = float(input('Digite o seu salário bruto: R$ '))

# Inicializa o valor do imposto de renda
imposto_de_renda = 0

# Calcula o imposto de renda com base nas faixas de renda
if salario_bruto <= 1903.98:
    print('Você é isento de imposto de renda.')
elif salario_bruto <= 2826.65:
    imposto_de_renda = (salario_bruto - 1903.99) * 0.075
elif salario_bruto <= 3751.05:
    imposto_de_renda = (2826.65 - 1903.99) * 0.075 + (salario_bruto - 2826.66) * 0.15
elif salario_bruto <= 4664.68:
    imposto_de_renda = (2826.65 - 1903.99) * 0.075 + (3751.05 - 2826.66) * 0.15 + (salario_bruto - 3751.06) * 0.225
else:
    imposto_de_renda = (2826.65 - 1903.99) * 0.075 + (3751.05 - 2826.66) * 0.15 + (4664.68 - 3751.06) * 0.225 + (salario_bruto - 4664.69) * 0.275

# Calcula o salário líquido subtraindo o imposto de renda do salário bruto
salario_liquido = salario_bruto - imposto_de_renda

# Exibe o salário bruto, o imposto de renda e o salário líquido
if salario_bruto > 1903.98:
    print(f'Salário Bruto: R$ {salario_bruto:.2f}')
    print(f'Imposto de Renda: R$ {imposto_de_renda:.2f}')
    print(f'Salário Líquido: R$ {salario_liquido:.2f}')

