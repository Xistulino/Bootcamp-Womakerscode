# Manipulação de arquivos

file = 'arquivo.txt'

#open somente para leitura
arquivo_leitura = open(file, 'r')

# abertura para escrita
arquivo_escrita = open(file, 'w')
arquivo_escrita.write('Texto a ser escrito')

#abertura de arquivos binários
arquivo_leitura = open(file, 'wb')