"""Escreva um programa que calcule o tempo de uma viagem. Faça um
comparativo do mesmo percurso de avião, carro e ônibus.
Levando em consideração:
● avião = 600 km/h
● carro = 100 km/h
● ônibus = 80 km/h
"""


distancia = float(input('Escreva a distância do percurso em km: '))

aviao = 600
carro = 100
onibus = 80

tempo_aviao = distancia / aviao
tempo_carro = distancia / carro
tempo_onibus = distancia / onibus

print(f'O tempo de viagem de avião é: {tempo_aviao:.2f} horas')
print(f'O tempo de viagem de carro é: {tempo_carro:.2f} horas')
print(f'O tempo de viagem de ônibus é: {tempo_onibus:.2f} horas')