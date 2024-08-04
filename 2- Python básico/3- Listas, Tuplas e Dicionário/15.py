#Tuplas são listas que não podem ter valores alterados


lista_frutas = [] # declaração da lista
fruta = input('Digite sua fruta: ') # quando quero que um usuário digite algo faço uma variável 
lista_frutas.append(fruta)


lista_frutas.append('Maça')
lista_frutas.append('Uva')
lista_frutas.append('Banana')
print(lista_frutas)


tupla = ('maça', 'uva', 'banana') # declaração para tupla
print(tupla)