"""
Receba do usuário a quantidade de litros de combustível consumidos e
a distância percorrida. Calcule e imprima o consumo médio em km/l.
"""

km_percorrido = float(input('Digite a distância percorrida: '))
litro_combustivel = float(input('Digite a quantidade de litros de combustível consumido: '))

calculo = km_percorrido/litro_combustivel

print(f'Km percorrido: {km_percorrido:.2f}Km ')
print(f'Litros de combustível consumidos: {litro_combustivel:.2f}L')
print(f'O consumo médio é {calculo:.2f}Km/L')