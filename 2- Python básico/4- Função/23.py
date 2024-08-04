# Tratamentos de exceções: Possíveis erros que podem ocorrer

def divisao(a,b):
    try:
        resultado = a/b
        print(resultado)
    except ZeroDivisionError: # ele coloca o erro de uma forma clara 
        print('Erro: Impossível dividir um valor por zero')
    except TypeError as e: #
        print(f'Erro: O tipo de dado informado está incorreto. \n Detalhes: {e}')
    else:
        print('Sem exceções')
#divisao(10,0)
#divisao(10,2)

divisao(10, 'string')

# try = tente
# except = excessões para tratamento de exceções 