# Um risco de importar tudo é ter uma outra função ou variável no namespace
# atual com o mesmo nome. Neste caso, é fácil ter um bug porque você pode
# ao invés de usar um método, o programador acaba usando o outro.

from funcoes_de_log import * # o risco de usar o * não é uma boa prática

imprimir_no_log(f'Bem vinda, {nome_do_usuario}!')
print()

def imprimir_no_log(texto):
    print(texto)

imprimir_no_log(f'Bem vinda, {nome_do_usuario}')