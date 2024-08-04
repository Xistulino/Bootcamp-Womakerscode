# Lista - Pode receber uma informação pois são mutáveis

"""
Lista = []
lista.append('Maça')
print(lista)

frutas = ['maça', 'laranja', 'morango']
frutas.append('uva')
print(frutas)

for fruta in frutas:
    print(fruta)
"""

lista_frutas = [] # declaração da lista
fruta = input('Digite sua fruta: ') # quando quero que um usuário digite algo faço uma variável 
lista_frutas.append(fruta)


lista_frutas.append('Maça')
lista_frutas.append('Uva')
lista_frutas.append('Banana')
print(lista_frutas)


