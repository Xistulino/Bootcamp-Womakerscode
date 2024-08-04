'''Faça um Programa que peça a quantidade de quilômetros, transforme
em metros, centímetros e milímetros.'''

km = float(input('Digite a quantidade de quilômetros percorrido:  '))

m = km * 1000
cm = km * 100000
mm = km * 1000000

print(f'Você percorreu {km:.2f} km, que equivalem a:')
print(f'Metros: {m:.2f} m')
print(f'Centímetros: {cm:.2f} cm')
print(f'Milímetros: {mm:.2f} mm')