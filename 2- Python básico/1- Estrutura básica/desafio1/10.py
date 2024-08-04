"""
Faça um Programa que utilize 4 variáveis como preferir e no final print
uma mensagem amigável utilizando as variáveis criadas.
Exemplos de variáveis: nome, idade, lugar, profissão ....
Exemplo de retorno: Olá Maria, prazer te conhecer. Sou de São Paulo
também e estou migrando de área.
"""

nome = str(input('Digite seu nome: '))
apelido = str(input('Digite seu apelido: '))
comida = str(input('Digite sua comida favorita: '))
time = str(input('Digite seu time do coaração: '))

print(f'Olá {nome}, vou te chamar de {apelido}, pois é seu apelido. Sua comida favorita é {comida} e seu time do coração é {time}')