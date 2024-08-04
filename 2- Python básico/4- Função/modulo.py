from datetime import datetime
ano_primeira_medalha = 1996
categoria_medalha = 'Volei de praia'
tipo_medalha = 'ouro'

ano_atual = datetime.now().year

mensagem_olimpica = (
    f'Nos jogos {ano_primeira_medalha} a dupla feminina "{tipo_medalha}"ano_primeira_medalha'
    f'Vinte anos depois {categoria_medalha}'
)

print(mensagem_olimpica)

#Cálculo dos anos desde conquista
anos_passados = ano_atual - ano_primeira_medalha
print(f'Já se passaram {anos_passados} anos da conquista')