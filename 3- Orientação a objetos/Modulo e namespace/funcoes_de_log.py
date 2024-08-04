# Este arquivo consiste no módulo "funcoes_do_log"
nome_do_usuario = 'Dori'

def imprimir_no_log(texto,nível='info'):
    if nível == 'info':
        print(f'[INFO:] {texto}')
    elif nível == 'alerta':
        print(f'[ALERTA] {texto}')
    elif nível == 'erro':
        print(f'[ERRO] {texto}')
    else:
        print(f'[ERRO] Nível {nível}. Não não é válido!')